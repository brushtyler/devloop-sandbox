import unittest

from widget import slugify, unslugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify("  "), "")

    def test_max_length_default_keeps_whole_slug(self):
        self.assertEqual(slugify("Hello big world"), "hello-big-world")
        self.assertEqual(slugify("Hello big world", max_length=None), "hello-big-world")

    def test_max_length_fits_exactly(self):
        self.assertEqual(slugify("Hello big world", max_length=15), "hello-big-world")

    def test_max_length_cuts_at_word_boundary(self):
        self.assertEqual(slugify("Hello big world", max_length=9), "hello-big")

    def test_max_length_never_ends_with_dash(self):
        self.assertEqual(slugify("Hello big world", max_length=8), "hello")

    def test_max_length_truncates_long_first_word(self):
        self.assertEqual(slugify("Supercalifragilistic", max_length=5), "super")

    def test_max_length_on_empty_text(self):
        self.assertEqual(slugify("  ", max_length=3), "")

    def test_max_length_below_one_raises(self):
        with self.assertRaises(ValueError):
            slugify("Hello", max_length=0)
        with self.assertRaises(ValueError):
            slugify("Hello", max_length=-1)


class UnslugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(unslugify("hello-world"), "Hello World")

    def test_empty_parts(self):
        self.assertEqual(unslugify("--a--b-"), "A B")

    def test_empty(self):
        self.assertEqual(unslugify(""), "")


if __name__ == "__main__":
    unittest.main()
