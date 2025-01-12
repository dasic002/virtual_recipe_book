from django.contrib import admin
from .models import Recipe, Comment, Rating, Favourite, Ingredient
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'listing_type', 'approved', 'updated_on', 'created_on')
    search_fields = ['title', 'description']
    list_filter = ('approved', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Ingredient)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('food_item', 'recipe')
    search_fields = ['recipe', 'food_item']
    list_filter = ('recipe',)


@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('body', 'recipe', 'author', 'approved')
    search_fields = ['recipe', 'author', 'body']
    list_filter = ('recipe', 'author',  'created_on')


@admin.register(Rating)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('score', 'recipe', 'author', 'approved')
    search_fields = ['recipe', 'score', 'author']
    list_filter = ('recipe', 'author', 'score', 'created_on')


# Register your models here.
admin.site.register(Favourite)