import unittest
from app.services.validation import is_email, normalize_phone, is_phone, password_problems


class TestValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_email("student@college.ru"))

    def test_invalid_email(self):
        self.assertFalse(is_email("не почта"))

    def test_normalize_phone(self):
        self.assertEqual(normalize_phone("8 (900) 123-45-67"), "+79001234567")

    def test_invalid_phone_raises(self):
        with self.assertRaises(ValueError):
            normalize_phone("123")

    def test_is_phone(self):
        self.assertTrue(is_phone("8 (900) 123-45-67"))
        self.assertFalse(is_phone("123"))

    def test_password_valid(self):
        self.assertEqual(password_problems("Qwerty12345"), [])


if __name__ == "__main__":
    unittest.main()
