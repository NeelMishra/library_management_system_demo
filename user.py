class User:
    """
    Represents a user within the system.
    """
    def __init__(self, name: str, user_id: str) -> None:
        if not name or not user_id:
            raise ValueError("Name and user ID must be provided.")
        self.name = name
        self.user_id = user_id

    def __str__(self) -> str:
        """
        Returns a string representation of the User instance, useful for debugging and logging.".
        """
        return f"User({self.name}, {self.user_id})"

