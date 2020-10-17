from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from recipe.models import Recipe, Favorite, Purchase


# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': '이미 존재하는 계정입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        # User wants to enter info
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': '계정 또는 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'account/signup.html')


def mypage(request):
    purchase_list = Purchase.objects.filter(user_id=request.user)
    if Favorite.objects.filter(user_id=request.user).count() != 0:
        recipe_list = []
        for fav in Favorite.objects.filter(user_id=request.user):
            recipe_list += Recipe.objects.filter(id=fav.recipe_id)
        return render(request, 'account/mypage.html', {'recipe_list': recipe_list, 'purchase_list': purchase_list})
    else:
        return render(request, 'account/mypage.html', {'purchase_list': purchase_list})
