from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="요리의 종류")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(blank=True, help_text="요리법에 대한 사진")
    description = models.CharField(max_length=200, help_text="요리법에 대한 설명")

    def __str__(self):
        return self.description


class Ingredient(models.Model):
    name = models.CharField(max_length=200, help_text="재료의 이름")
    amount = models.CharField(max_length=200, help_text="재료의 양")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, help_text="요리의 이름")
    subtitle = models.TextField(max_length=1000, help_text="요리에 대한 간략한 설명")
    profile = models.ImageField(blank=True, help_text="요리에 대한 사진")
    genre = models.ManyToManyField(Genre)
    ingredient = models.ManyToManyField(Ingredient)
    image = models.ManyToManyField(Image)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])


class Favorite(models.Model):
    recipe_id = models.CharField(max_length=200, help_text="요리법의 아이디")
    user_id = models.CharField(max_length=200, help_text="유저 아이디")

    def __str__(self):
        return self.user_id
