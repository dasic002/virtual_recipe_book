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
