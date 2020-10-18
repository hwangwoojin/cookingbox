from django.contrib import admin
from recipe.models import Recipe, Genre, Image, Ingredient, Favorite, Product, Purchase, SecretIngredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Ingredient)
admin.site.register(Favorite)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(SecretIngredient)