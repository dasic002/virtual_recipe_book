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
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.author}"