from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


def index(request):
    return render(request, 'main/index.html')


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'main/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = 'main/movie.html'
