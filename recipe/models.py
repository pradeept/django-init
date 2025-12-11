from typing import override
from django.db import models

# Create your models here.

class Recipe(models.Model):

    @override
    def __str__(self):
        return self.recipe_name

    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField(max_length=500)
    recipe_image = models.ImageField(upload_to="recipes")
