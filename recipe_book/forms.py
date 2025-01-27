from django.forms import inlineformset_factory, Textarea
from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Comment, Recipe, Ingredient


class CommentForm(forms.ModelForm):
    '''
    Class for form for comments
    '''
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            "body": Textarea(attrs={
                "rows": 5,
                "class": 'dark-bg'}),
        }


class RecipeForm(forms.ModelForm):
    '''
    Class for form for recipe

    feature_image field currently excluded from form as it is not working
    correctly and causing form not to validate and save the rest of the data.
    '''
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
    '''
    Class for form for ingredient
    '''
    class Meta:
        model = Ingredient
        fields = (
            'food_item',
            'quantity',
            'unit',
        )

# Creates formset for our dynamically manipulated form to save multiple
# instances of ingredients in one submission.
IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    min_num=0,
    extra=1,
    can_delete=True
)
