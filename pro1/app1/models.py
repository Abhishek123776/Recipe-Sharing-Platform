from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50) 

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    comment = models.TextField(null=True)


