# api/views.py
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD operations
    for the Book model (list, create, retrieve, update, delete).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Permission Classes to Views
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

