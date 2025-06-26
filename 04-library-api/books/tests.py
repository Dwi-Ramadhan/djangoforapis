from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape
from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A Great Book's Title",
            subtitle="An Excellent Book's Subtitle",
            author="Dwi Ramadhan Rivaldo",
            isbn="1234567891011",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A Great Book's Title")
        self.assertEqual(self.book.subtitle, "An Excellent Book's Subtitle")
        self.assertEqual(self.book.author, "Dwi Ramadhan Rivaldo")
        self.assertEqual(self.book.isbn, "1234567891011")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape("Excellent Book's Subtitle"))
        self.assertTemplateUsed(response, "books/book_list.html")
