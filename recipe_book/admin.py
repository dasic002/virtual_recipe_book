from django.contrib import admin
from .models import Recipe, Comment, Rating, Favourite

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favourite)