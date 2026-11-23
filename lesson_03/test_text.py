import unittest
from app.utils.text import clean_spaces, shorten, initials, slug


class TestText(unittest.TestCase):
    def test_clean_spaces(self):
        self.assertEqual(clean_spaces("  один   два "), "один два")

    def test_shorten_keeps_short_text(self):
        self.assertEqual(shorten("кот", 5), "кот")

    def test_shorten_long_text(self):
        self.assertEqual(shorten("abcdef", 4), "abc…")

    def test_initials(self):
        self.assertEqual(initials("Пётр Иванович Смирнов"), "П. И. Смирнов")

    def test_initials_empty(self):
        with self.assertRaises(ValueError):
            initials("  ")

    def test_slug(self):
        self.assertEqual(slug("Отчёт за март"), "otchet-za-mart")


if __name__ == "__main__":
    unittest.main()
