from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Ingredient, Category, Rating
from .serializers import RecipeSerializer,RatingSerializer,CategorySerializer,IngredientSerializer
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CategorySerializer(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientSerializer(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer