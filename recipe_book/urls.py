from . import views
from django.urls import path

urlpatterns = [
    path('profile/<slug:author>/', views.user_library, name='user_library'),
    path('recipe-create/', views.recipe_create, name='recipe_create'),
    path('', views.RecipeLibrary, name='home'),
    path('<slug:slug>/edit-recipe', views.recipe_edit, name='recipe_edit'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]