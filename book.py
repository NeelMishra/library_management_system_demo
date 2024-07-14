class Book:
    """
    Represents a single book in a library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book, must be unique.
    """
    def __init__(self, title: str, author: str, isbn: str) -> None:
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN must be provided and non-empty.")
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"
