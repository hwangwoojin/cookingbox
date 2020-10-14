from django.contrib import admin
from home.models import Recipe, Author, Genre

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Author)
admin.site.register(Genre)
