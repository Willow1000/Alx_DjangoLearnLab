from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book
from datetime import date

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=date(1958, 1, 1),
            author=self.author
        )
        self.book_url = reverse("book-list")  # Ensure named routes in router

    def test_authenticated_create_book(self):
        """Test creating a book via API with authentication"""
        self.client.login(username="testuser", password="testpassword")  # Authenticate user
        data = {
            "title": "No Longer at Ease",
            "publication_year": "1960-01-01",
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["title"], data["title"])

    def test_authenticated_get_books(self):
        """Test retrieving book list with authentication"""
        self.client.login(username="testuser", password="testpassword")  # Authenticate user
        response = self.client.get(self.book_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)  # If using pagination
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_authenticated_update_book(self):
        """Test updating a book with authentication"""
        self.client.login(username="testuser", password="testpassword")  # Authenticate user
        update_url = reverse("book-detail", args=[self.book.id])
        data = {"title": "Updated Book Title"}

        response = self.client.patch(update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book Title")

    def test_authenticated_delete_book(self):
        """Test deleting a book with authentication"""
        self.client.login(username="testuser", password="testpassword")  # Authenticate user
        delete_url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_unauthenticated_create_book_fails(self):
        """Ensure an unauthenticated user cannot create a book"""
        data = {
            "title": "Arrow of God",
            "publication_year": "1964-01-01",
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Adjust if using different auth settings

    def test_unauthenticated_update_book_fails(self):
        """Ensure an unauthenticated user cannot update a book"""
        update_url = reverse("book-detail", args=[self.book.id])
        data = {"title": "Unauthorized Update"}

        response = self.client.patch(update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_delete_book_fails(self):
        """Ensure an unauthenticated user cannot delete a book"""
        delete_url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
