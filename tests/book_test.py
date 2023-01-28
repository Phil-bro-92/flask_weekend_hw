import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("Game of Thrones", "George R R Martin", "Fantasy")

    def test_book_has_title(self):
        book_title = self.book_1.title
        self.assertEqual("Game of Thrones", book_title)

    def test_book_has_author(self):
        book_author = self.book_1.author
        self.assertEqual("George R R Martin", book_author)

    def test_book_has_genre(self):
        book_genre = self.book_1.genre
        self.assertEqual("Fantasy", book_genre)
