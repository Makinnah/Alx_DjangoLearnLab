from django.db import models
from relationship_app.models import CustomUser  # if needed

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    published_date = models.DateField()
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
