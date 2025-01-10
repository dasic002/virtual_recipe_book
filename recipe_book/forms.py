from django.forms import inlineformset_factory, ModelForm, modelformset_factory, Textarea
from .models import Comment, Recipe, Ingredient
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            "body": Textarea(attrs={
                "rows": 5,
                "class": 'dark-bg'}),
        }
        

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'prep_time',
            'cook_time',
            'servings',
            'method',
            'listing_type',
            'source',
            'source_url',
        )
        

# RecipeFormset = modelformset_factory(
#     Recipe,
#     fields = (
#             'title',
#             'description',
#             'prep_time',
#             'cook_time',
#             'servings',
#             'method',
#             'listing_type',
#             'source',
#             'source_url',
#         )
# )


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            'food_item',
            'quantity',
            'unit',
        )


IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    min_num=1,
    extra=0,
    can_delete=False
)