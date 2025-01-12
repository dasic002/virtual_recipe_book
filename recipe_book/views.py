from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template import loader
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Comment, Recipe, User
from .forms import CommentForm, IngredientFormSet, RecipeForm


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
    recipe_list = Recipe.objects.filter(approved=2)
    sample_list = Recipe.objects.filter(approved=2).filter(author=1)
    template = loader.get_template('recipe_book/index.html')

    paginator = Paginator(recipe_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'recipe_list': recipe_list,
        'sample_list': sample_list,
        'page_obj': page_obj
    }
    
    return HttpResponse(template.render(context, request))


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
        First instance of request.user.id and related recipe from :model:`recipe_book.Favourite`.  

    **Template:**

    :template:`recipe_book/recipe_detail.html`
    """  
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    ratings = recipe.ratings.filter(approved=2)
    user_rating = ratings.filter(author=request.user.id).first()
    comments = recipe.comments.all().order_by("-created_on")
    comment_form = CommentForm()
    faved = recipe.saves.filter(author=request.user.id).first()

        
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "recipe": recipe,
            "ratings": ratings,
            "user_rating": user_rating,
            "comments": comments,
            "comment_form": comment_form,
            "faved": faved,
        },
    )


# @login_required
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
                f'Recipe {recipe.title} saved! If you have set the recipe public it will be awaiting approval'
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


def user_library(request, author):
    """
    Display user's collection of recipes :model:`recipe_book.Recipe`.

    **Context**

    ``recipes_created``
        A set of instances related to user as author from
        :model:`recipe_book.Recipe`.

    **Template:**

    :template:`recipe_book/recipe_detail.html`
    """  
    author = get_object_or_404(User, username=author)
    recipes_created = Recipe.objects.filter(author=author).order_by("-created_on")
    template = loader.get_template('recipe_book/user_library.html')

    paginator = Paginator(recipes_created, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'recipes_created': recipes_created,
        'page_obj': page_obj,
        'author': author,
    }
    
    return HttpResponse(template.render(context, request))


    
# @login_required
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

        if recipe_form.is_valid() and ingredient_form.is_valid() and request.user == recipe.author:
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
                f'Recipe {recipe.title} updated! If you have set the recipe public it will be awaiting approval'
            )

            return redirect('user_library', recipe.author.username)

    
    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientFormSet(instance=recipe)

    return render(
        request,
        "recipe_book/recipe_editor.html",
        {
            "recipe_form": recipe_form,
            "ingredient_form": ingredient_form,
        },
    )


def recipe_delete(request, id):
    """
    Deletes user's existing recipe from :model:`recipe_book.Recipe`.

    **Context**

    ``recipe_form``
        Form modelled from :model:`recipe_book.Recipe`.

    ``ingredient_form``
        Formset linked to :model:`recipe_book.Recipe`
        linked via the foregin key of recipe.
    
    **Template:**

    :template:`recipe_book/user_library.html`
    """ 
    recipe = Recipe.objects.get(id=id)
    username = recipe.author.username

    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, f'Recipe {recipe.title} deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own recipes!')

    return redirect('user_library', username)


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.approved = 0
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))