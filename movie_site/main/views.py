from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


def index(request):
    return render(request, 'main/index.html')


class MoviesView(View):
    """Movies list"""
    def get(self, request):
        movie_list = Movie.objects.all()
        context = {"movie_list": movie_list}
        return render(request, 'main/movies.html', context)


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        context = {"movie": movie}
        return render(request, 'main/movie.html', context)