from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Book endpoints
        self.list_url = reverse("book-list")   # from router or URL patterns
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])

        # Sample book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Things Fall Apart", str(response.data))

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Things Fall Apart - Updated"}
        response = self.client.patch(self.detail_url(self.book.id), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart - Updated")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.detail_url(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Things")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        Book.objects.create(title="A Man of the People", publication_year=1966, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
