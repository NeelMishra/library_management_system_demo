import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Test creating a user with valid inputs."""
        user = User("John Doe", "001")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.user_id, "001")

    def test_user_creation_empty_name(self):
        """Test creating a user with an empty name should raise ValueError."""
        with self.assertRaises(ValueError):
            User("", "001")

    def test_user_creation_empty_user_id(self):
        """Test creating a user with an empty user_id should raise ValueError."""
        with self.assertRaises(ValueError):
            User("John Doe", "")

if __name__ == '__main__':
    unittest.main()
