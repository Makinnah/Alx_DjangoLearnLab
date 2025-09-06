from django.contrib import admin
from .models import Book

# Register the Book model with custom display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    list_filter = ('author', 'publication_year')            # Filters in sidebar
    search_fields = ('title', 'author')                     # Search box

