import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation_success(self):
        """Test creating a book with valid inputs."""
        book = Book("Python Programming", "John Doe", "1234567890")
        self.assertEqual(book.title, "Python Programming")
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.isbn, "1234567890")

    def test_book_creation_empty_title(self):
        """Test creating a book with an empty title should raise ValueError."""
        with self.assertRaises(ValueError):
            Book("", "John Doe", "1234567890")

    def test_book_creation_empty_author(self):
        """Test creating a book with an empty author should raise ValueError."""
        with self.assertRaises(ValueError):
            Book("Python Programming", "", "1234567890")

    def test_book_creation_empty_isbn(self):
        """Test creating a book with an empty ISBN should raise ValueError."""
        with self.assertRaises(ValueError):
            Book("Python Programming", "John Doe", "")

    def test_book_str_representation(self):
        """Test the string representation of a book."""
        book = Book("Python Programming", "John Doe", "1234567890")
        self.assertEqual(str(book), "Python Programming by John Doe, ISBN: 1234567890")

if __name__ == '__main__':
    unittest.main()
