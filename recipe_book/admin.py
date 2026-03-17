from django.contrib import admin
from .models import Recipe, Comment, Rating, Favourite, Ingredient
from django_summernote.admin import SummernoteModelAdmin


# Following the codestar blog walkthrough project
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    '''
    Register the recipe model in the admin panel including the summernote library.
    '''

    # the fields to include in the list of recipes.
    list_display = ('title', 'slug', 'author', 'listing_type', 'approved',
        'updated_on', 'created_on')
    
    # parameters to search recipes by.
    search_fields = ['title', 'description']
    
    # list of fields to quickly filter the list by. This list appears on the
    # right handside.
    list_filter = ('approved', 'created_on')

    # prepopulated the slug field for the recipe with the title written in the
    # title field.
    prepopulated_fields = {'slug': ('title',)}

    # sets the fields to include the text formatting enabled by summernote.
    summernote_fields = ('method',)


@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):
    '''
    Register the ingredient model in the admin panel including the summernote library.
    '''

    # the fields to include in the list of ingredients.
    list_display = ('__str__', 'recipe')

    # parameters to search ingredients by.
    search_fields = ['recipe', 'food_item']
    
    # list of fields to quickly filter the list by. This list appears on the
    # right handside.
    list_filter = ('recipe',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    '''
    Register the comment model in the admin panel including the summernote library.
    '''

    # the fields to include in the list of comments.
    list_display = ('id', 'body', 'recipe', 'author', 'approved')

    # parameters to search comments by.
    search_fields = ['recipe', 'author', 'body']
    
    # list of fields to quickly filter the list by. This list appears on the
    # right handside.
    list_filter = ('recipe', 'author',  'created_on')


@admin.register(Rating)
class RatingAdmin(SummernoteModelAdmin):
    '''
    Register the rating model in the admin panel including the summernote library.
    '''

    # the fields to include in the list of ratings.
    list_display = ('score', 'recipe', 'author', 'approved')

    # parameters to search ratings by.
    search_fields = ['recipe', 'score', 'author']
    
    # list of fields to quickly filter the list by. This list appears on the
    # right handside.
    list_filter = ('recipe', 'author', 'score', 'created_on')


@admin.register(Favourite)
class FavouriteAdmin(SummernoteModelAdmin):
    '''
    Register the Favourite model in the admin panel including the summernote library.
    '''

    # the fields to include in the list of favourites.
    list_display = ('__str__', 'recipe', 'author', 'added_on')

    # parameters to search favourites by.
    search_fields = ['recipe', 'author']
    
    # list of fields to quickly filter the list by. This list appears on the
    # right handside.
    list_filter = ('recipe', 'author', 'added_on')
