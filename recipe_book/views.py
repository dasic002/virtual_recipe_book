from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeLibrary(generic.ListView):
    queryset = Recipe.objects.filter(approved=2)
    template_name = "index.html"
    paginate_by = 6