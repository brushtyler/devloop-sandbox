import unittest

from widget import slugify, unslugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify("  "), "")


class UnslugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(unslugify("hello-world"), "Hello World")

    def test_empty_parts(self):
        self.assertEqual(unslugify("--a--b-"), "A B")

    def test_empty(self):
        self.assertEqual(unslugify(""), "")


if __name__ == "__main__":
    unittest.main()
