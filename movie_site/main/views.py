from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'main/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'main/login_page.html', context)


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            form.save()
            return redirect('login_page')

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
