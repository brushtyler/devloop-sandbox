import unittest

from widget import is_slug, slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify("  "), "")


class IsSlugTest(unittest.TestCase):
    def test_valid_slug(self):
        self.assertTrue(is_slug("hello-world"))

    def test_invalid_slugs(self):
        for text in ("Hello-World", "hello--world", "-hello", ""):
            with self.subTest(text=text):
                self.assertFalse(is_slug(text))


if __name__ == "__main__":
    unittest.main()
