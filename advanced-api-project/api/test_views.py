from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering,
    and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data and authenticated user.
        Runs before each test.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.author = Author.objects.create(name="George Orwell")

        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"

    # ------------------------
    # READ OPERATIONS
    # ------------------------

    def test_list_books(self):
        """Unauthenticated users can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Unauthenticated users can retrieve a single book"""
        url = f"/api/books/{self.book1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    # ------------------------
    # CREATE OPERATION
    # ------------------------

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username='testuser', password='testpassword')

        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2000,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ------------------------
    # UPDATE OPERATION
    # ------------------------

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username='testuser', password='testpassword')

        url = f"/api/books/{self.book1.id}/update/"
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    # ------------------------
    # DELETE OPERATION
    # ------------------------

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username='testuser', password='testpassword')

        url = f"/api/books/{self.book1.id}/delete/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------------
    # FILTERING
    # ------------------------

    def test_filter_books_by_year(self):
        """Filter books by publication year"""
        response = self.client.get(f"{self.list_url}?publication_year=1945")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Animal Farm")

    # ------------------------
    # SEARCHING
    # ------------------------

    def test_search_books_by_title(self):
        """Search books by title"""
        response = self.client.get(f"{self.list_url}?search=1984")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    # ------------------------
    # ORDERING
    # ------------------------

    def test_order_books_by_publication_year_desc(self):
        """Order books by publication year descending"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.data[0]['publication_year'], 1949)
