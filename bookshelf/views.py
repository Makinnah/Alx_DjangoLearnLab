from django.shortcuts import render
from .forms import SearchForm
from .models import Book

def search_books(request):
    form = SearchForm(request.POST or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'results': results})
