from . import views
from django.urls import path

urlpatterns = [
    path('profile/<slug:author>/', views.user_library, name='user_library'),
    path('recipe-create/', views.recipe_create, name='recipe_create'),
    path('', views.RecipeLibrary, name='home'),
    path('<slug:id>/delete-recipe', views.recipe_delete, name='recipe_delete'),
    path('<slug:slug>/edit-recipe', views.recipe_edit, name='recipe_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/browse', views.sample_recipe_detail, name='sample_recipe_detail'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]