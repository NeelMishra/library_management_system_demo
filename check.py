class Checkout:
    """Represents a single book checkout in the library system."""
    
    def __init__(self, user_id: str, isbn: str):
        if not user_id or not isbn:
            raise ValueError("User ID and ISBN must not be empty.")
        self.user_id = user_id
        self.isbn = isbn
    
    def __str__(self):
        return f"Checkout(User ID: {self.user_id}, ISBN: {self.isbn})"

class CheckoutManager:
    """Manages book checkouts in the library system."""
    
    def __init__(self):
        self.checkouts = {}  # Dictionary to track checkouts by ISBN

    def checkout_book(self, user_id: str, isbn: str):
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
        self.checkouts[isbn] = Checkout(user_id, isbn)
        print(f"Book {isbn} checked out to user {user_id}.")

    def find_checkout(self, isbn: str):
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

# Example usage of the CheckoutManager
if __name__ == "__main__":
    checkout_manager = CheckoutManager()
    try:
        checkout_manager.checkout_book("001", "9783161484100")  # Successful checkout
        print(checkout_manager.find_checkout("9783161484100"))
        checkout_manager.checkout_book("002", "9783161484100")  # Attempt to checkout an already checked out book
    except Exception as e:
        print(e)  # Handle the error by printing it out
