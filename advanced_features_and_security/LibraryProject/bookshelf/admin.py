from django.contrib import admin
from .models import Author, Library, Book

admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Book)
