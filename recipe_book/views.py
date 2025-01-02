from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeLibrary(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipe_book/recipe_library.html"