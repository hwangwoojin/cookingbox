from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Recipe, Favorite


# Create your views here.
class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipe/index.html'


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'


def favorite(request):
    if request.method == 'POST':
        if Favorite.objects.filter(user_id=request.user).filter(recipe_id=request.POST['recipe_id']).count() == 0:
            fav = Favorite()
            fav.recipe_id = request.POST['recipe_id']
            fav.user_id = str(request.user)
            fav.save()
        return HttpResponseRedirect('/recipe/'+request.POST['recipe_id'])


def defavorite(request):
    if request.method == 'POST':
        fav = Favorite.objects.filter(recipe_id=request.POST['recipe_id'], user_id=request.user)
        fav.delete()
        return redirect('/account/mypage/')
    else:
        return render(request, 'account/mypage.html')
