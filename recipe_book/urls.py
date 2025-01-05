from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeLibrary, name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]