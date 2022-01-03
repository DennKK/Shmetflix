from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    url = models.SlugField(max_length=160, unique=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    """ Actors and Directors """
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    url = models.SlugField(max_length=160, unique=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300, default='')
    description = models.TextField(default="")
    poster = models.ImageField(default=None, upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2022)
    country = models.CharField(max_length=100, default="")
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    genre = models.ManyToManyField(Genre)
    world_premiere = models.DateField(date.today, default=None)
    budget = models.PositiveIntegerField(help_text="$", default=0)
    worldwide = models.PositiveIntegerField(default=0, help_text="$")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True, default="")
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie_shot"
        verbose_name_plural = "Movie_shots"


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating_star"
        verbose_name_plural = "Rating_stars"


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="star", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CharField)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating_star"
        verbose_name_plural = "Rating_stars"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50, default="USER")
    parent = models.ForeignKey('self', verbose_name="Parent", blank=True, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"