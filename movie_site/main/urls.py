from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('movies/', views.MoviesView.as_view()),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('register/', views.register_page, name="register_page"),
]