from django.contrib import admin
from .models import Recipe, Comment, Rating, Favourite, Ingredient
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'approved')
    search_fields = ['title']
    list_filter = ('approved',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favourite)
admin.site.register(Ingredient)