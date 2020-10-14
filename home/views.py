from django.shortcuts import render
from home.models import Recipe, Author, Genre


# Create your views here.
def index(request):
    return render(request, 'home/index.html')