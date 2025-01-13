from django.forms import inlineformset_factory, Textarea
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Comment, Recipe, Ingredient


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
    # featured_image = CloudinaryFileField()

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
            # 'featured_image',
        )


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
    min_num=0,
    extra=1,
    can_delete=True
)
