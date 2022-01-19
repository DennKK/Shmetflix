from django.shortcuts import render
from .models import Movie, Genre, Actor


def index(request):
    return render(request, 'main/index.html')


def movies(request):
    movie_list = Movie.objects.all()
    context = {"movie_list": movie_list}
    return render(request, 'main/movies.html', context)


def movie(request, movie_id):
    movie_id = Movie.objects.filter(id=movie_id)
    context = {"movie_id": movie_id}
    return render(request, 'main/movie.html', context)
