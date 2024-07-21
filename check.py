import re
class Checkout:
    """Represents a single book checkout in the library system."""
    
    def __init__(self, user_id: str, isbn: str):
        # user_id input validation : Potential failures => user_id is empty, or not an alphanumeric string
        if not user_id:
            raise ValueError("User ID must be provided and cannot be empty.")
        if not isinstance(user_id, str) or not user_id.isdigit(): # We can also have user_id to be integer, but I have set it to string to ensure standardization.
            raise ValueError("User ID must be numeric string.")
        # isbin input validation : Potential failures => isbin is empty or not a valid ISBN number
        if not isbn:
            raise ValueError("ISBN must not be empty and must be a valid ISBN.")
        if not re.match(r'^\d{10}(\d{3})?$', isbn): # Using the same ISBN regex as in the Book class for consistency (check wiki for more information on ISBN : https://en.wikipedia.org/wiki/ISBN)
            raise ValueError("ISBN must be a valid 10 or 13 digit number without spaces or hyphens.")
        
        self.user_id = user_id.strip()
        self.isbn = isbn.strip()
    
    def __str__(self):
        return f"Checkout(User ID: {self.user_id}, ISBN: {self.isbn})"
    
