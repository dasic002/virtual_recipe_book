from django.db import models
from django.contrib.auth.models import User

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


# Create your models here.
class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="own_recipes"
        )
    # feature_image = 
    description = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    method = models.JSONField(null=False)
    listing_type = models.IntegerField(choices=LIST_TYPE, default=0)
    approved = models.IntegerField(choices=STATUS, default=0)
    origin = models.ForeignKey(
        'Recipe',
        on_delete = models.SET_NULL,
        blank=True,
        null=True,
        related_name="remixes"
        )
    source_url = models.URLField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} by {self.author}"


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

    class Meta:
        ordering = ["created_on"]
    
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
        choices=((i,i) for i in range(1, 6))
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

    class Meta:
        ordering = ["-created_on"]
    
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
        related_name="saved_recipe"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collector"
    )
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_on"]
    
    def __str__(self):
        return f"{self.recipe.title} - saved by {self.author}"