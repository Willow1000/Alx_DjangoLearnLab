from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book
from datetime import date

from rest_framework.authtoken.models import Token

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test users, authentication, and sample data"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass")

        self.author = Author.objects.create(name="Ngugi wa Thiong'o")
        self.book = Book.objects.create(
            title="The River Between",
            publication_year=date(2025, 3, 8),
            author=self.author
        )

        self.token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin_user)

    def authenticate(self, admin=False):
        """Helper function to authenticate user"""
        token = self.admin_token if admin else self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_unauthorized_access(self):
        """Ensure unauthorized users cannot access the endpoints"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_books_authenticated(self):
        """Ensure authenticated users can list books"""
        self.authenticate()
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_without_permission(self):
        """Ensure normal users cannot create a book"""
        self.authenticate()
        data = {"title": "Petals of Blood", "publication_year": "2024-06-15", "author": self.author.id}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_with_admin_permission(self):
        """Ensure admin users can create a book"""
        self.authenticate(admin=True)
        data = {"title": "Petals of Blood", "publication_year": "2024-06-15", "author": self.author.id}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_permission(self):
        """Ensure normal users cannot update books"""
        self.authenticate()
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_update_book(self):
        """Ensure admins can update book details"""
        self.authenticate(admin=True)
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book_permission(self):
        """Ensure only admins can delete books"""
        self.authenticate()
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_book(self):
        """Ensure admins can delete books"""
        self.authenticate(admin=True)
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
