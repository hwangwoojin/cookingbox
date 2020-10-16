from django.views import generic
from recipe.models import Recipe


# Create your views here.
#def index(request):
    #return render(request, 'recipe/index.html')

class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipe/index.html'


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'
