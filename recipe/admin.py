from django.contrib import admin
from recipe.models import Recipe, Genre, Image

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Genre)
admin.site.register(Image)
