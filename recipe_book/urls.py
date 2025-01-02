from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeLibrary.as_view(), name='home'),
]