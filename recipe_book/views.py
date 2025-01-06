from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
# from django.views import generic
from .models import Recipe, Comment, Rating, Favourite, Ingredient
import statistics


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

    **Template:**

    :template:`recipe_book/recipe_detail.html`
    """

    def average_score(data):
        list_score = []
        for x in data:
            list_score.append(x.score)
        
        if len(list_score) > 0:
            list_score = statistics.mean(list_score)
        else:
            list_score = None

        return list_score
    

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    rating = recipe.ratings.filter(approved=2)
    score = average_score(rating)
    faved = recipe.saves.filter(author=request.user.id)
    # faved = recipe.saves.values_list('author', flat=True)
    

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "recipe": recipe,
            "rating": rating,
            "score": score,
            "faved": faved,
        },
    )