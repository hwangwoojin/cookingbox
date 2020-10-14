from django.db import models
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, help_text="요리의 이름")
    subtitle = models.TextField(max_length=1000, help_text="요리에 대한 간략한 설명")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="요리의 종류")

    def __str__(self):
        return self.name
