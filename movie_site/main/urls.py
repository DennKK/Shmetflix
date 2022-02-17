from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('movies/', views.MoviesView.as_view(), name='movies'),
    path('movie/<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/register/', views.register_page, name="register_page"),
]