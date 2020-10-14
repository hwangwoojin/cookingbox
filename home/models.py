from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    """Model representing a recipe genre."""
    name = models.CharField(max_length=200, help_text='Enter a recipe genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Recipe(models.Model):
    """Model representing a recipe (but not a specific copy of a recipe)."""
    title = models.CharField(max_length=200)
    subtitle = models.TextField(max_length=1000, help_text='Enter a brief description of the recipe')
    # Foreign Key used because recipe can only have one author, but authors can have multiple recipes
    # Author as a string rather than object because it hasn't been declared yet in the file.
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because genre can contain many recipes. Recipes can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this recipe')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this recipe."""
        return reverse('recipe-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
