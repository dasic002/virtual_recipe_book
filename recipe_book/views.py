from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
# from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm, IngredientFormSet, RecipeForm


# Create your views here.
# class RecipeLibrary(generic.ListView):
#     queryset = Recipe.objects.filter(approved=2)
#     template_name = "index.html"
#     paginate_by = 6


def RecipeLibrary(request):
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
            print("recipe", recipe)
            for ingredient in ingredients:
                print(ingredient)
                ingredient.recipe = recipe
                print(ingredient)
                ingredient.save()

            

            messages.add_message(
                request, messages.SUCCESS,
                'Recipe saved! If you have set the recipe public it will be awaiting approval'
            )


    return render(
        request,
        "recipe_book/recipe_editor.html",
        {
            "recipe_form": recipe_form,
            "ingredient_form": ingredient_form,
        },
    )