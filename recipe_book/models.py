from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
import statistics

LIST_TYPE = (
    (0, "DRAFT"),
    (1, "PRIVATE"),
    (2, "UNLISTED"),
    (3, "PUBLISHED")
)

STATUS = (
    (0, "REVIEW"),
    (1, "REJECTED"),
    (2, "APPROVED")
)


# Follows a similar format to the Post model in the walkthrough project
class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="own_recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    prep_time = models.PositiveIntegerField(default=1)
    cook_time = models.PositiveIntegerField(default=1)
    servings = models.PositiveIntegerField(default=1)
    method = models.TextField(blank=True)
    listing_type = models.IntegerField(choices=LIST_TYPE, default=0)
    approved = models.IntegerField(choices=STATUS, default=0)
    origin = models.ForeignKey(
        'Recipe',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="remixes"
    )
    source = models.CharField(max_length=250, blank=True)
    source_url = models.URLField(max_length=250, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # sets the order fo recipes to list the most recent first
    class Meta:
        ordering = ["-created_on"]

    # sets the string of a recipe record to the format of
    # "<recipe title> by <recipe author>"
    def __str__(self):
        return f"{self.title} by {self.author}"

    # creates the slug automatically from the title string
    # followed the last example in this link
    # https://learndjango.com/tutorials/django-slug-tutorial
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # set as a property we can call, this function will create an iterable list
    # of all the scores for the given recipe. Then using the statistics library
    # mean function, to calculate the average score.
    @property
    def average_score(self):
        list_score = self.ratings.values_list('score', flat=True)

        if len(list_score) > 0:
            list_score = round(statistics.mean(list_score), 1)
        else:
            list_score = None

        return list_score

    # set as a property we can call, this function will collect the ingredients
    # for a given recipe and format it in a human legible list before rendering
    # to the recipe detail page.
    @property
    def ingredients(self):
        list_ingredients = self.ingredients_needed.all()
        for line in list_ingredients:
            line.quantity = line.quantity.normalize()
            line.unit = line.Unit.__call__(line.unit).label
        return list_ingredients

    # Set as a property we can all, this function will unpack the JSON values
    # as if it were a dictionary into a list of tuples so we can iterate
    # through into the method table.
    # Redundant whilst method is stored as a textfield rather than JSON.
    @property
    def steps(self):
        return self.method.items()


# Follows a similar format to the Post model in the walkthrough project
class Comment(models.Model):
    """
    Stores a single Recipe comment entry related to
    :model:`recipe_book.Recipe`.
    :model:`auth.User`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="commenter"
    )
    body = models.TextField()
    approved = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    # sets the order fo comments to list the most recent first
    class Meta:
        ordering = ["created_on"]

    # sets the string of a comment record to the format of
    # "<comment body> by <comment author>"
    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Rating(models.Model):
    """
    Stores a single Recipe rating entry related to
    :model:`recipe_book.Recipe`.
    :model:`auth.User`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="ratings"
    )
    score = models.IntegerField(
        default=0,
        choices=((i, i) for i in range(1, 6))
    )
    review = models.CharField(max_length=250, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reviewer"
    )
    approved = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    # sets the order fo ratings to list the most recent first
    class Meta:
        ordering = ["-created_on"]

    # sets the string of a rating record to the format of
    # "<recipe title> - rated by <rating author>"
    def __str__(self):
        return f"{self.recipe.title} - rated by {self.author}"


class Favourite(models.Model):
    """
    Stores a single saved Recipe entry for the given user related to
    :model:`recipe_book.Recipe`.
    :model:`auth.User`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="saves"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collector"
    )
    added_on = models.DateTimeField(auto_now_add=True)

    # sets the order fo ratings to list the most recent first
    class Meta:
        ordering = ["-added_on"]

    # sets the string of a favourite record to the format of
    # "<recipe title> - saved by <favourite author>"
    def __str__(self):
        return f"{self.recipe.title} - saved by {self.author}"


class Ingredient(models.Model):
    """
    Stores a single ingredient and quantity entry for a given Recipe
    related to :model:`recipe_book.Recipe`.
    """

    # defines the class of units of measurement, to only be used for
    # ingredients
    class Unit(models.IntegerChoices):
        PIECE = 0, "pc"
        STICK = 1, "stick"
        MILLIGRAM = 2, "mg"
        GRAM = 3, "g"
        KILOGRAM = 4, "kg"
        OUNCE = 5, "oz"
        POUND = 6, "lb"
        MILLILITERS = 7, "ml"
        CENTILITERS = 8, "cl"
        LITERS = 9, "l"
        TEASPOON = 10, "tsp"
        TABLESPOON = 11, "tbsp"
        FLUID_OUNCE = 12, "floz"
        CUP = 13, "cup"
        PINT = 14, "pint"
        QUART = 15, "quart"
        GALLON = 16, "gallon"

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="ingredients_needed"
    )
    food_item = models.CharField()
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.IntegerField(
        choices=Unit.choices,
        default=Unit.PIECE
    )

    # Converts the unit of measurement into a human legible format by
    # enumerating the the integer stored against the Unit class and stores it
    # as the unit variable to call again. Then, sets the string of an
    # ingredient record to the format of
    # "<ingredient quantity><ingredient unit label> <ingredient food_item>
    # used in <recipe title>"
    def __str__(self):
        self.unit = self.Unit.__call__(self.unit)
        return (f"{self.quantity}{self.unit.label} {self.food_item} " +
                f"used in {self.recipe.title}")
