import unittest

from widget import slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify("  "), "")


if __name__ == "__main__":
    unittest.main()
