import re

class Book:
    """
    Represents a single book in a library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book, must be unique.
    """
    def __init__(self, title: str, author: str, isbn: str) -> None:
        # title input validation : Potential failures => title is empty string
        if not title:
            raise ValueError("Title must be provided and must be non-empty.")
        # author input validation : Potential failures => author is empty string
        if not author:
            raise ValueError("Author must be provided and must be non-empty.")
        # isbn input validation : Potential failures => isbn is empty string, or isbn is not a valid ISBN number
        if not isbn:
            raise ValueError("ISBN must be provided and must be non-empty.")
        if not re.match(r'^\d{10}(\d{3})?$', isbn): # Check for a ISBN format validation (assuming ISBN-10 or ISBN-13 without hyphens)(check wikipedia : https://en.wikipedia.org/wiki/ISBN for more information)
            raise ValueError("ISBN must be a valid 10 or 13 digit number without spaces or hyphens.")
        
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"
