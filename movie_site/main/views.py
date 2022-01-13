from django.shortcuts import render
from .models import Movie, Genre


def index(request):
    return render(request, 'main/index.html')


def movies(request):
    movie_list = Movie.objects.all()
    context = {"movie_list": movie_list}
    return render(request, 'main/movies.html', context)