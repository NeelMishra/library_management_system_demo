from book import Book
from check import Checkout
from user import User
from storage import Storage

class BookManager:
    """
    Manages a collection of books in a library.
    
    Attributes:
        books (dict): A dictionary storing Book instances, keyed by ISBN.
        storage (Storage): The storage handler for persistence.
    """
    def __init__(self, storage: Storage):
        self.books = {}  # Dictionary for efficient book access by ISBN
        self.storage = storage
        self._load_books()

    def _load_books(self) -> None:
        """Loads books from storage into the manager."""
        books = self.storage.get_books()
        for book in books:
            self.books[book.isbn] = book

    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Adds a new Book to the collection, ensuring no duplicate ISBNs.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN number of the book.

        Raises:
            ValueError: If a book with the same ISBN already exists, or if any field is empty.
        """
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN must be provided and non-empty.")
        if isbn in self.books:
            raise ValueError("A book with the same ISBN already exists.")
        book = Book(title, author, isbn)
        self.books[isbn] = book
        self.storage.add_book(book)

    def list_books(self) -> None:
        """Lists all the books in the collection."""
        for book in self.books.values():
            print(" * ", book)

    def find_book_by_isbn(self, isbn: str) -> Book:
        """
        Finds a book by its ISBN.

        Args:
            isbn (str): The ISBN to search for.

        Returns:
            Book: The book with the matching ISBN.

        Raises:
            LookupError: If no book with the specified ISBN exists.
        """
        try:
            return self.books[isbn]
        except KeyError:
            raise LookupError("No book found with the specified ISBN.")

    def remove_book_by_isbn(self, isbn: str) -> None:
        """
        Removes a book by its ISBN from the collection.

        Args:
            isbn (str): The ISBN of the book to remove.

        Raises:
            LookupError: If no book with the specified ISBN exists.
        """
        if isbn in self.books:
            del self.books[isbn]
            self.storage.remove_entry("books", isbn, "isbn")
        else:
            raise LookupError("No book found with the specified ISBN to remove.")


class CheckoutManager:
    """Manages book checkouts in the library system."""
    
    def __init__(self, storage: Storage):
        self.checkouts = {}  # Dictionary to track checkouts by ISBN
        self.storage = storage
        self._load_checkouts()

    def _load_checkouts(self) -> None:
        """Loads checkouts from storage into the manager."""
        checkouts = self.storage.get_checkouts()
        for checkout in checkouts:
            self.checkouts[checkout.isbn] = checkout

    def checkout_book(self, user_id: str, isbn: str) -> None:
        """Checkout a book to a user.

        Args:
            user_id (str): The ID of the user checking out the book. Must not be empty.
            isbn (str): The ISBN of the book to checkout. Must not be empty.

        Raises:
            ValueError: If the book is already checked out or if user_id or isbn is empty.
        """
        if not user_id or not isbn:
            raise ValueError("User ID and ISBN must not be empty.")
        if isbn in self.checkouts:
            raise ValueError("This book is already checked out.")
        checkout = Checkout(user_id, isbn)
        self.checkouts[isbn] = checkout
        self.storage.add_checkout(checkout)
        print(f"Book {isbn} checked out to user {user_id}.")

    def find_checkout(self, isbn: str) -> Checkout:
        """Finds which user has checked out a book by ISBN.

        Args:
            isbn (str): The ISBN of the book.

        Returns:
            Checkout: The checkout information.

        Raises:
            KeyError: If the book is not currently checked out.
        """
        if isbn not in self.checkouts:
            raise KeyError("This book is not checked out.")
        return self.checkouts[isbn]


class UserManager:
    """
    Manages a collection of users in the system.
    
    Attributes:
        users (dict): A dictionary storing User instances, keyed by user ID.
        storage (Storage): The storage handler for persistence.
    """
    def __init__(self, storage: Storage):
        self.users = {}  # Dictionary for efficient user fetching
        self.storage = storage
        self._load_users()

    def _load_users(self) -> None:
        """Loads users from storage into the manager."""
        users = self.storage.get_users()
        for user in users:
            self.users[user.user_id] = user

    def add_user(self, name: str, user_id: str) -> None:
        """
        Adds a new User to the collection, ensuring unique user IDs.

        Args:
            name (str): The full name of the user.
            user_id (str): A unique identifier for the user.

        Raises:
            ValueError: If a user with the same user_id already exists or if the user_id is empty.
        """
        if not name or not user_id:
            raise ValueError("Name and user ID must not be empty.")
        if user_id in self.users:
            raise ValueError("A user with this ID already exists.")
        user = User(name, user_id)
        self.users[user_id] = user
        self.storage.add_user(user)

    def get_user(self, user_id: str) -> User:
        """
        Retrieves a User by their user_id.

        Args:
            user_id (str): The unique identifier of the user to retrieve.

        Returns:
            User: The User object associated with the provided user_id.

        Raises:
            KeyError: If no user with the given user_id exists.
        """
        if not user_id:
            raise ValueError("User ID must not be empty.")
        try:
            return self.users[user_id]
        except KeyError:
            raise KeyError("User not found.")

    def list_users(self) -> None:
        """Lists all the users in the system."""
        for user in self.users.values():
            print(" * ", user)

    def remove_user(self, user_id: str) -> None:
        """
        Removes a user by their user_id from the collection.

        Args:
            user_id (str): The user_id of the user to remove.

        Raises:
            KeyError: If no user with the specified user_id exists.
        """
        if user_id in self.users:
            del self.users[user_id]
            self.storage.remove_entry("users", user_id, "user_id")
        else:
            raise KeyError("No user found with the specified user ID to remove.")
