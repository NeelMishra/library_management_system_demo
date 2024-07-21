class User:
    """
    Represents a user within the system.
    """
    def __init__(self, name: str, user_id: str) -> None:
        # Name input validation : Potential failures => name is empty, or not a string.
        if not name:
            raise ValueError("Name must be provided and cannot be empty.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        # user_id input validation : Potential failures => user_id is empty, or not an alphanumeric string
        if not user_id:
            raise ValueError("User ID must be provided and cannot be empty.")
        if not isinstance(user_id, str) or not user_id.isdigit():
            raise TypeError("User ID must be a numeric string.")

        self.name = name.strip()
        self.user_id = user_id.strip()

    def __str__(self) -> str:
        """
        Returns a string representation of the User instance, useful for debugging and logging.".
        """
        return f"User({self.name}, {self.user_id})"
