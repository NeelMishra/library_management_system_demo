import unittest
from check import Checkout

class TestCheckout(unittest.TestCase):
    def test_checkout_creation_success(self):
        """Test creating a checkout with valid inputs."""
        checkout = Checkout("001", "9783161484100")
        self.assertEqual(checkout.user_id, "001")
        self.assertEqual(checkout.isbn, "9783161484100")

    def test_checkout_creation_empty_user_id(self):
        """Test creating a checkout with an empty user_id should raise ValueError."""
        with self.assertRaises(ValueError):
            Checkout("", "9783161484100")

    def test_checkout_creation_empty_isbn(self):
        """Test creating a checkout with an empty ISBN should raise ValueError."""
        with self.assertRaises(ValueError):
            Checkout("001", "")

    def test_checkout_str_representation(self):
        """Test the string representation of a checkout."""
        checkout = Checkout("001", "9783161484100")
        self.assertEqual(str(checkout), "Checkout(User ID: 001, ISBN: 9783161484100)")

if __name__ == '__main__':
    unittest.main()
