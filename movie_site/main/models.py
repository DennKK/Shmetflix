from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    # Date Of Birth
    DOB = models.DateField()

    def __str__(self):
        return self.first_name


class Genre(models.Model):
    name = models.CharField(default='IDONTKNOW', max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    age_limit = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.title