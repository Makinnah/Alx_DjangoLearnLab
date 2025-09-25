from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#DRF's Generic Views
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve, update, or delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can update/delete
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


#Comments
# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Public list view — returns all books (GET /api/books/)
class ListView(generics.ListAPIView):
    """
    Public list endpoint for Book model.
    - GET: anyone can list books (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create view — authenticated users only (POST /api/books/create/)
class CreateView(generics.CreateAPIView):
    """
    Create a new Book instance.
    - POST: authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Detail view — public retrieve (GET /api/books/<pk>/)
class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single Book by primary key.
    - GET: anyone can retrieve
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Update view — authenticated users only (PUT/PATCH /api/books/<pk>/update/)
class UpdateView(generics.UpdateAPIView):
    """
    Update an existing Book.
    - PUT / PATCH: authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete view — authenticated users only (DELETE /api/books/<pk>/delete/)
class DeleteView(generics.DestroyAPIView):
    """
    Delete a Book.
    - DELETE: authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

