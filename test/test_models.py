import unittest
from unittest.mock import MagicMock
from library_management_system_demo.book import Book
from library_management_system_demo.check import Checkout
from library_management_system_demo.user import User
from library_management_system_demo.storage import Storage
from library_management_system_demo.models import BookManager, CheckoutManager, UserManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        """Create a BookManager instance with a mocked storage before each test."""
        self.mock_storage = MagicMock(Storage)
        self.manager = BookManager(self.mock_storage)
        self.mock_storage.get_books.return_value = []

    def test_add_book_success(self):
        """Test adding a book successfully."""
        self.manager.add_book("Python Programming", "John Doe", "1234567890")
        self.assertIn("1234567890", self.manager.books)
        self.assertEqual(self.manager.books["1234567890"].title, "Python Programming")
        self.mock_storage.add_book.assert_called_once()

    def test_add_book_duplicate_isbn(self):
        """Test adding a book with a duplicate ISBN should raise ValueError."""
        self.manager.add_book("Python Programming", "John Doe", "1234567890")
        with self.assertRaises(ValueError):
            self.manager.add_book("Advanced Python", "Jane Smith", "1234567890")

    def test_add_book_empty_title(self):
        """Test adding a book with an empty title should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_book("", "John Doe", "1234567890")

    def test_add_book_empty_author(self):
        """Test adding a book with an empty author should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_book("Python Programming", "", "1234567890")

    def test_add_book_empty_isbn(self):
        """Test adding a book with an empty ISBN should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_book("Python Programming", "John Doe", "")

    def test_list_books(self):
        """Test listing all books."""
        self.manager.add_book("Python Programming", "John Doe", "1234567890")
        self.manager.add_book("Advanced Python", "Jane Smith", "0987654321")
        self.manager.list_books()  # Should print the list of books

    def test_find_book_by_isbn_success(self):
        """Test finding a book by its ISBN successfully."""
        self.manager.add_book("Python Programming", "John Doe", "1234567890")
        book = self.manager.find_book_by_isbn("1234567890")
        self.assertEqual(book.title, "Python Programming")

    def test_find_book_by_isbn_not_found(self):
        """Test finding a book by an ISBN that does not exist should raise LookupError."""
        with self.assertRaises(LookupError):
            self.manager.find_book_by_isbn("9999999999")

    def test_remove_book_by_isbn_success(self):
        """Test removing a book by its ISBN successfully."""
        self.manager.add_book("Python Programming", "John Doe", "1234567890")
        self.manager.remove_book_by_isbn("1234567890")
        self.assertNotIn("1234567890", self.manager.books)
        self.mock_storage.remove_entry.assert_called_once()

    def test_remove_book_by_isbn_not_found(self):
        """Test removing a book by an ISBN that does not exist should raise LookupError."""
        with self.assertRaises(LookupError):
            self.manager.remove_book_by_isbn("9999999999")


class TestCheckoutManager(unittest.TestCase):
    def setUp(self):
        """Create a CheckoutManager instance with a mocked storage before each test."""
        self.mock_storage = MagicMock(Storage)
        self.manager = CheckoutManager(self.mock_storage)
        self.manager.user_manager.add_user("John Doe", "001")
        self.manager.book_manager.add_book("test_book", "test_author", "9783161484100")
        self.mock_storage.get_checkouts.return_value = []

    def test_checkout_book_success(self):
        """Test checking out a book successfully."""
        self.manager.checkout_book("001", "9783161484100")
        self.assertIn("9783161484100", self.manager.checkouts)
        self.assertEqual(self.manager.checkouts["9783161484100"].user_id, "001")
        self.mock_storage.add_checkout.assert_called_once()

    def test_checkout_book_already_checked_out(self):
        """Test checking out a book that is already checked out should raise ValueError."""
        self.manager.checkout_book("001", "9783161484100")
        with self.assertRaises(ValueError):
            self.manager.checkout_book("002", "9783161484100")

    def test_checkout_book_empty_user_id(self):
        """Test checking out a book with an empty user_id should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.checkout_book("", "9783161484100")

    def test_checkout_book_empty_isbn(self):
        """Test checking out a book with an empty ISBN should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.checkout_book("001", "")

    def test_find_checkout_success(self):
        """Test finding a checkout by ISBN successfully."""
        self.manager.checkout_book("001", "9783161484100")
        checkout = self.manager.find_checkout("9783161484100")
        self.assertEqual(checkout.user_id, "001")

    def test_find_checkout_not_found(self):
        """Test finding a checkout by an ISBN that is not checked out should raise KeyError."""
        with self.assertRaises(KeyError):
            self.manager.find_checkout("9783161484100")


class TestUserManager(unittest.TestCase):
    def setUp(self):
        """Create a UserManager instance with a mocked storage before each test."""
        self.mock_storage = MagicMock(Storage)
        self.manager = UserManager(self.mock_storage)
        self.mock_storage.get_users.return_value = []

    def test_add_user_success(self):
        """Test adding a user successfully."""
        self.manager.add_user("John Doe", "001")
        self.assertIn("001", self.manager.users)
        self.assertEqual(self.manager.users["001"].name, "John Doe")
        self.mock_storage.add_user.assert_called_once()

    def test_add_user_duplicate_id(self):
        """Test adding a user with a duplicate ID should raise ValueError."""
        self.manager.add_user("John Doe", "001")
        with self.assertRaises(ValueError):
            self.manager.add_user("Jane Doe", "001")

    def test_add_user_empty_name(self):
        """Test adding a user with an empty name should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_user("", "002")

    def test_add_user_empty_user_id(self):
        """Test adding a user with an empty user ID should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_user("Jane Doe", "")

    def test_get_user_success(self):
        """Test retrieving an existing user."""
        self.manager.add_user("John Doe", "001")
        user = self.manager.get_user("001")
        self.assertEqual(user.name, "John Doe")

    def test_get_user_nonexistent(self):
        """Test retrieving a non-existent user should raise KeyError."""
        with self.assertRaises(KeyError):
            self.manager.get_user("002")

    def test_get_user_empty_user_id(self):
        """Test retrieving a user with an empty user ID should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.get_user("")

    def test_list_users(self):
        """Test listing all users."""
        self.manager.add_user("John Doe", "001")
        self.manager.add_user("Jane Doe", "002")
        self.manager.list_users()  # Should print the list of users

    def test_remove_user_success(self):
        """Test removing a user by their user ID successfully."""
        self.manager.add_user("John Doe", "001")
        self.manager.remove_user("001")
        self.assertNotIn("001", self.manager.users)
        self.mock_storage.remove_entry.assert_called_once()

    def test_remove_user_nonexistent(self):
        """Test removing a user by a non-existent user ID should raise KeyError."""
        with self.assertRaises(KeyError):
            self.manager.remove_user("999")

if __name__ == '__main__':
    unittest.main()
