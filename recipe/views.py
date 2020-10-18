from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Recipe, Favorite, Product, Purchase


# Create your views here.
class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipe/index.html'


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'


def favorite(request):
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


def buy(request):
    recipe = Recipe.objects.get(id=request.POST['recipe_id'])
    ingredient_list = []
    secret_ingredient_list = []
    for ingredient in recipe.ingredient.all().order_by('name'):
        product_list = []
        product_list += Product.objects.filter(name=ingredient.name)
        ingredient_list.append(product_list)
    for ingredient in recipe.secret_ingredient.all().order_by('name'):
        product_list = []
        product_list += Product.objects.filter(name=ingredient.name)
        secret_ingredient_list.append(product_list)
    return render(request, 'recipe/buy.html', {'recipe': recipe, 'ingredient_list': ingredient_list, 'secret_ingredient_list': secret_ingredient_list})


def purchase(request):
    pur = Purchase()
    pur.recipe_id = request.POST['recipe_id']
    pur.user_id = str(request.user)
    pur.product = request.POST['product']
    pur.price = request.POST['price']
    pur.save()
    return HttpResponseRedirect('/account/mypage/')


def search(request):
    query = request.POST['search']
    recipe_list = Recipe.objects.filter(title__contains=str(query))
    return render(request, 'recipe/search.html', {'recipe_list': recipe_list, 'query': query})
