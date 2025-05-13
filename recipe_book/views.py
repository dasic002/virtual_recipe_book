from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template import loader
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from .models import Comment, Recipe, User, Favourite, Rating
from .forms import CommentForm, RatingForm, IngredientFormSet, RecipeForm


# Create your views here.
def RecipeLibrary(request):
    """
    Displays published recipe instances from :model:`recipe_book.Recipe`.

    **Context**

    ``recipe_list``
        A set of instances of published recipes from
        :model:`recipe_book.Recipe`.

    ``sample_list``
        A set of instances of published recipes from first author from
        :model:`recipe_book.Recipe` to use as examples for new visitors.

    **Template:**

    :template:`recipe_book/index.html`
    """
    recipe_list = Recipe.objects.filter(approved=2).filter(listing_type=3)

    sample_list = recipe_list.order_by('created_on')[:3]

    if request.user.is_authenticated:
        for recipe in recipe_list:
            if recipe.saves.filter(author=request.user).first() is not None:
                recipe.liked_by_user = recipe.saves.filter(author=request.user).first()

    template = loader.get_template('recipe_book/index.html')

    paginator = Paginator(recipe_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'recipe_list': recipe_list,
        'sample_list': sample_list,
        'page_obj': page_obj,
    }

    return HttpResponse(template.render(context, request))


def sample_recipe_detail(request, slug):
    """
    Display an individual recipe from a sample set of 3 instances of
    :model:`recipe_book.Recipe`.
    Otherwise throw error 403 Forbidden

    **Context**

    ``recipe``
        An instance of :model:`recipe_book.Recipe`.

    ``ratings``
        A set of instances related to current recipe from
        :model:`recipe_book.Rating`.

    ``user_rating``
        First instance of request.user.id and related recipe from
        :model:`recipe_book.Rating`.

    ``comments``
        A set of instances related to current Recipe from
        :model:`recipe_book.Comment`.

    ``faved``
        First instance of request.user.id and related recipe from
        :model:`recipe_book.Favourite`.

    **Template:**

    :template:`recipe_book/recipe_detail.html`
    """
    sample_list = Recipe.objects.all().filter(approved=2).order_by(
        'created_on')[:3]
    requested_obj = Recipe.objects.filter(slug=slug).first()

    if requested_obj in sample_list:
        recipe = get_object_or_404(Recipe.objects.all(), slug=slug)
    else:
        raise PermissionDenied

    ratings = recipe.ratings.filter(approved=2)
    user_rating = ratings.filter(author=request.user.id).first()
    rating_form = RatingForm()
    comments = recipe.comments.all().order_by("-created_on")
    comment_form = CommentForm()
    faved = recipe.saves.filter(author=request.user.id).first()

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "recipe": recipe,
            "ratings": ratings,
            "user_rating": user_rating,
            "rating_form": rating_form,
            "comments": comments,
            "comment_form": comment_form,
            "faved": faved,
        },
    )


@login_required
def recipe_detail(request, slug):
    """
    Display an individual :model:`recipe_book.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe_book.Recipe`.

    ``ratings``
        A set of instances related to current recipe from
        :model:`recipe_book.Rating`.

    ``user_rating``
        First instance of request.user.id and related recipe from
        :model:`recipe_book.Rating`.

    ``comments``
        A set of instances related to current Recipe from
        :model:`recipe_book.Comment`.

    ``faved``
        First instance of request.user.id and related recipe from
        :model:`recipe_book.Favourite`.

    **Template:**

    :template:`recipe_book/recipe_detail.html`
    """
    queryset = Recipe.objects.filter(
        Q(listing_type='2') | Q(listing_type='3') | Q(author=request.user)
        )
    
    recipe = get_object_or_404(queryset, slug=slug)
    
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        comment_form = CommentForm(request.POST)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.author = request.user
            rating.recipe = recipe
            rating.approved = 0
            rating.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Rating submitted and awaiting approval'
            )
            rating_form = RatingForm()

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            comment_form = CommentForm()

    else:
        rating_form = RatingForm()
        comment_form = CommentForm()

    ratings_list = recipe.ratings.all().order_by("-created_on")
    user_rating = ratings_list.filter(author=request.user.id).first()
    ratings = ratings_list.exclude(author=request.user.id)
    
    rating_form = RatingForm()
    comments = recipe.comments.all().order_by("-created_on")
    comment_form = CommentForm()
    faved = recipe.saves.filter(author=request.user.id).first()

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "recipe": recipe,
            "ratings": ratings,
            "user_rating": user_rating,
            "rating_form": rating_form,
            "comments": comments,
            "comment_form": comment_form,
            "faved": faved,
        },
    )


@login_required
def recipe_create(request):
    """
    Add new recipe to :model:`recipe_book.Recipe`.

    **Context**

    ``recipe_form``
        Form modelled from :model:`recipe_book.Recipe`.

    ``ingredient_form``
        Formset linked to :model:`recipe_book.Recipe`
        linked via the foregin key of recipe.

    **Template:**

    :template:`recipe_book/recipe_editor.html`
    """
    recipe_form = RecipeForm()
    ingredient_form = IngredientFormSet()

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        ingredient_form = IngredientFormSet(data=request.POST)

        if recipe_form.is_valid() and ingredient_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            ingredients = ingredient_form.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()

            messages.add_message(
                request, messages.SUCCESS,
                (f'Recipe {recipe.title} saved! If you have set the recipe ' +
                    f'public it will be awaiting approval')
            )

            return redirect('user_library', recipe.author.username)

    return render(
        request,
        "recipe_book/recipe_editor.html",
        {
            "recipe_form": recipe_form,
            "ingredient_form": ingredient_form,
        },
    )


@login_required
def user_library(request, author):
    """
    Display users' collection of recipes :model:`recipe_book.Recipe`.

    **Context**

    ``recipes_list``
        A set of instances related to author from
        :model:`recipe_book.Recipe`. Conditionally
        filtered, if user is the author of queryset
        they will see all, regardless of approved state.
        Otherwise, if viewing another user's library,
        the request use can only view the approved and
        published or unlisted recipes.

    **Template:**

    :template:`recipe_book/user_library.html`
    """
    author = get_object_or_404(User, username=author)
    if request.user == author:
        recipe_list = Recipe.objects.filter(
            author=author).order_by("-created_on")
    else:
        recipe_list = Recipe.objects.filter(
            author=author).filter(approved=2).filter(
                listing_type=3).order_by("-created_on")

    for recipe in recipe_list:
        if recipe.saves.filter(author=request.user).first() is not None:
            recipe.liked_by_user = recipe.saves.filter(author=request.user).first()

    template = loader.get_template('recipe_book/user_library.html')

    paginator = Paginator(recipe_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'recipe_list': recipe_list,
        'page_obj': page_obj,
        'author': author,
    }

    return HttpResponse(template.render(context, request))


@login_required
def user_faves(request, author):
    """
    Display users' collection of favourite recipes
    :model:`recipe_book.Recipe`.

    **Context**

    ``faves_list``
        A set of instances related to author from
        :model:`recipe_book.Favourite`.

    **Template:**

    :template:`recipe_book/user_faves.html`
    """
    author = get_object_or_404(User, username=author)
    faves_list = Recipe.objects.filter(
        saves__author=author).order_by("-created_on")

    for recipe in faves_list:
        if recipe.saves.filter(author=request.user).first() is not None:
            recipe.liked_by_user = recipe.saves.filter(author=request.user).first()
    
    template = loader.get_template('recipe_book/user_faves.html')

    paginator = Paginator(faves_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'faves_list': faves_list,
        'page_obj': page_obj,
        'author': author,
    }

    return HttpResponse(template.render(context, request))


@login_required
def recipe_edit(request, slug):
    """
    Edits user's existing recipe from :model:`recipe_book.Recipe`.

    **Context**

    ``recipe_form``
        Form modelled from :model:`recipe_book.Recipe`.

    ``ingredient_form``
        Formset linked to :model:`recipe_book.Recipe`
        linked via the foregin key of recipe.

    **Template:**

    :template:`recipe_book/recipe_editor.html`
    """
    recipe = Recipe.objects.get(slug=slug)
    ingredients = recipe.ingredients_needed.first()
    ingredient_form = IngredientFormSet()

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        ingredient_form = IngredientFormSet(data=request.POST, instance=recipe)

        if (recipe_form.is_valid() and ingredient_form.is_valid() and
                request.user == recipe.author):
            recipe = recipe_form.save(commit=False)
            recipe.approved = 0
            recipe.save()
            ingredients = ingredient_form.save(commit=False)
            for obj in ingredient_form.deleted_objects:
                obj.delete()
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()

            messages.add_message(
                request, messages.SUCCESS,
                (f'Recipe {recipe.title} updated! If you have set the ' +
                    f'recipe public it will be awaiting approval')
            )

            return redirect('user_library', recipe.author.username)
        
        else:
            messages.add_message(
                request, messages.ERROR,
                (f'Recipe {recipe.title} has not been updated!' +
                    f' You may not have permission to edit this recipe!')
            )

    elif request.user == recipe.author:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientFormSet(instance=recipe)
    
    else:
        messages.add_message(
            request, messages.ERROR,
            ('You can only edit your own recipes!')
        )

        raise PermissionDenied

    return render(
        request,
        "recipe_book/recipe_editor.html",
        {
            "recipe_form": recipe_form,
            "ingredient_form": ingredient_form,
        },
    )


@login_required
def recipe_delete(request, id):
    """
    Deletes user's existing recipe from :model:`recipe_book.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe_book.Recipe`.

    **Template:**

    :template:`recipe_book/user_library.html`
    """
    recipe = Recipe.objects.get(id=id)
    username = recipe.author.username

    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(
            request, messages.SUCCESS,
            f'Recipe {recipe.title} deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own recipes!')

    return redirect('user_library', username)


@login_required
def recipe_fave(request, id):
    """
    Adds recipe to user's favourites from :model:`recipe_book.Recipe`,
    recording in :model:`recipe_book.Favourite`.

    **Context**

    ``recipe``
        An instance of :model:`recipe_book.Recipe`.
        
    ``favourite``
        An instance of :model:`recipe_book.Favourite`.

    **Template:**

        :template:`recipe_book/user_library.html`
    """
    next_url = request.GET.get('next', '/')
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.saves.filter(author=request.user).first() is None:
        recipe.saves.create(author=request.user)
        messages.add_message(
            request, messages.SUCCESS,
            f'Recipe {recipe.title} added to your favourites!')
    else:
        messages.add_message(
            request, messages.ERROR,
            f'Recipe {recipe.title} already in your favourites!')
    
    if is_valid_path(next_url):
        return redirect(next_url)
    else:
        return redirect('home')


@login_required
def recipe_unfave(request, id):
    """
    Removes recipe from user's favourites from :model:`recipe_book.Recipe`,
    removing from :model:`recipe_book.Favourite`.

    **Context**

    ``recipe``
        An instance of :model:`recipe_book.Recipe`.

    ``favourite``
        An instance of :model:`recipe_book.Favourite`.

    **Template:**

        :template:`recipe_book/user_library.html`
    """
    next_url = request.GET.get('next', '/')
    fave = get_object_or_404(Favourite, id=id)
    recipe = fave.recipe

    if fave is not None:
        fave.delete()
        messages.add_message(
            request, messages.SUCCESS,
            f'Recipe {recipe.title} removed from your favourites!')
    else:
        messages.add_message(
            request, messages.ERROR,
            f'Recipe {recipe.title} not in your favourites!')
    
    if is_valid_path(next_url):
        return redirect(next_url)
    else:
        return redirect('home')


@login_required
def rating_edit(request, slug, rating_id):
    """
    view to edit ratings
    """
    if request.method == "POST":

        rating = get_object_or_404(Rating, pk=rating_id)
        rating_form = RatingForm(data=request.POST, instance=rating)

        if rating_form.is_valid() and rating.author == request.user:
            rating = rating_form.save(commit=False)
            rating.approved = 0
            rating.save()
            messages.add_message(request, messages.SUCCESS, 'Rating Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating rating!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def rating_delete(request, slug, rating_id):
    """
    view to delete ratings
    """
    rating = get_object_or_404(Rating, pk=rating_id)

    if rating.author == request.user:
        rating.delete()
        messages.add_message(request, messages.SUCCESS, 'Rating deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own ratings!')

        raise PermissionDenied

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.approved = 0
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!')

        raise PermissionDenied

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
