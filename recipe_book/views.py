from django.core.paginator import Paginator
from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
# from django.views import generic
from .models import Recipe


# Create your views here.
# class RecipeLibrary(generic.ListView):
#     queryset = Recipe.objects.filter(approved=2)
#     template_name = "index.html"
#     paginate_by = 6


def RecipeLibrary(request):
    recipe_list = Recipe.objects.filter(approved=2)
    sample_list = Recipe.objects.filter(approved=2).filter(author=1)
    template = loader.get_template('index.html')

    paginator = Paginator(recipe_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'recipe_list': recipe_list,
        'sample_list': sample_list,
        'page_obj': page_obj
    }
    
    return HttpResponse(template.render(context, request))
