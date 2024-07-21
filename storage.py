import json
import os
from typing import Dict, Any, List
from book import Book
from user import User
from check import Checkout

class Storage:
    """
    Manages the storage and retrieval of data to and from a JSON file.

    Attributes:
        file_path (str): The path to the JSON file used for storage.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        """
        Loads data from the JSON file.

        Returns:
            dict: The data loaded from the file.
        """
        try:
            if not os.path.exists(self.file_path):
                return {"books": [], "users": [], "checkouts": []}
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON from the storage file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def save_data(self) -> None:
        """
        Saves the current state of data to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            raise Exception(f"An error occurred while saving data: {e}")

    def add_book(self, book: Book) -> None:
        """
        Adds a book to the storage.

        Args:
            book (Book): The book to add.
        """
        if any(book_dict['isbn'] == book.isbn for book_dict in self.data["books"]):
            raise ValueError("A book with this ISBN already exists.")
        self.data["books"].append({
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn
        })
        self.save_data()

    def get_books(self) -> List[Book]:
        """
        Retrieves all books from the storage.

        Returns:
            list: A list of Book instances.
        """
        return [Book(book_dict["title"], book_dict["author"], book_dict["isbn"]) for book_dict in self.data["books"]]

    def add_user(self, user: User) -> None:
        """
        Adds a user to the storage.

        Args:
            user (User): The user to add.
        """
        if any(user_dict['user_id'] == user.user_id for user_dict in self.data["users"]):
            raise ValueError("A user with this user ID already exists.")
        self.data["users"].append({
            "name": user.name,
            "user_id": user.user_id
        })
        self.save_data()

    def get_users(self) -> List[User]:
        """
        Retrieves all users from the storage.

        Returns:
            list: A list of User instances.
        """
        return [User(user_dict["name"], user_dict["user_id"]) for user_dict in self.data["users"]]

    def add_checkout(self, checkout: Checkout) -> None:
        """
        Adds a checkout to the storage.

        Args:
            checkout (Checkout): The checkout to add.
        """
        if any(checkout_dict['isbn'] == checkout.isbn for checkout_dict in self.data["checkouts"]):
            raise ValueError("This book is already checked out.")
        self.data["checkouts"].append({
            "user_id": checkout.user_id,
            "isbn": checkout.isbn
        })
        self.save_data()

    def get_checkouts(self) -> List[Checkout]:
        """
        Retrieves all checkouts from the storage.

        Returns:
            list: A list of Checkout instances.
        """
        return [Checkout(checkout_dict["user_id"], checkout_dict["isbn"]) for checkout_dict in self.data["checkouts"]]

    def remove_entry(self, key: str, entry_id: str, id_field: str) -> None:
        """
        Removes an entry from the data.

        Args:
            key (str): The key under which the entry is to be removed.
            entry_id (str): The ID of the entry to remove.
            id_field (str): The field that contains the ID in the entry.
        """
        self.data[key] = [entry for entry in self.data[key] if entry[id_field] != entry_id]
        self.save_data()

# Example usage
if __name__ == "__main__":
    storage = Storage("library_data.json")
    # Example of adding a book
    storage.add_book(Book("Python Programming", "John Doe", "1234567890"))
    # Example of retrieving books
    books = storage.get_books()
    for book in books:
        print(book)
    # Example of adding a user
    storage.add_user(User("Jane Doe", "001"))
    # Example of retrieving users
    users = storage.get_users()
    for user in users:
        print(user)
    # Example of adding a checkout
    storage.add_checkout(Checkout("001", "1234567890"))
    # Example of retrieving checkouts
    checkouts = storage.get_checkouts()
    for checkout in checkouts:
        print(checkout)
