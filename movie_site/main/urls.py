from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('movies/', views.MoviesView.as_view()),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
]