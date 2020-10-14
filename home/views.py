from django.shortcuts import render
from home.models import Recipe, Author, Genre


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_recipe = Recipe.objects.all().count()

    # The 'all()' is implied by default.
    num_author = Author.objects.count()

    context = {
        'num_recipe': num_recipe,
        'num_author': num_author,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)