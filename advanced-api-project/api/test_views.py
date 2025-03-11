from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from datetime import date

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Set up test data"""
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=date(1958, 1, 1),
            author=self.author
        )
        self.book_url = reverse("book-list")  # URL for book list (ensure named routes in router)

    def test_create_book(self):
        """Test creating a book via API"""
        data = {
            "title": "No Longer at Ease",
            "publication_year": "1960-01-01",
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["title"], data["title"])

    def test_get_books(self):
        """Test retrieving book list"""
        response = self.client.get(self.book_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)  # If using pagination
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_update_book(self):
        """Test updating a book"""
        update_url = reverse("book-detail", args=[self.book.id])
        data = {"title": "Updated Book Title"}

        response = self.client.patch(update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book Title")

    def test_delete_book(self):
        """Test deleting a book"""
        delete_url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
