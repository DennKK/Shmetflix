from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import CreateUserForm


def index(request):
    return render(request, 'main/index.html')


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main/register_page.html', context)


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'main/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = 'main/movie.html'
