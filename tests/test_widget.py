import unittest

from widget import is_slug, slugify, unslugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello_world")

    def test_empty(self):
        self.assertEqual(slugify("  "), "")

    def test_max_length_default_keeps_whole_slug(self):
        self.assertEqual(slugify("Hello big world"), "hello_big_world")
        self.assertEqual(slugify("Hello big world", max_length=None), "hello_big_world")

    def test_max_length_fits_exactly(self):
        self.assertEqual(slugify("Hello big world", max_length=15), "hello_big_world")

    def test_max_length_cuts_at_word_boundary(self):
        self.assertEqual(slugify("Hello big world", max_length=9), "hello_big")

    def test_max_length_never_ends_with_separator(self):
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


class SlugifySeparatorTest(unittest.TestCase):
    def test_default_separator_is_underscore(self):
        self.assertEqual(slugify("Hello, World!"), "hello_world")

    def test_dash_separator(self):
        self.assertEqual(slugify("Hello, World!", separator="-"), "hello-world")

    def test_max_length_counts_separator(self):
        self.assertEqual(slugify("Hello big world", max_length=9, separator="."), "hello.big")
        self.assertEqual(slugify("Hello big world", max_length=8, separator="."), "hello")

    def test_invalid_separator_raises(self):
        for separator in ("ab", "a", "1", "", "--"):
            with self.subTest(separator=separator):
                with self.assertRaises(ValueError):
                    slugify("x", separator=separator)


class SlugifyKeepCaseTest(unittest.TestCase):
    def test_keep_case(self):
        self.assertEqual(slugify("iPhone Case", keep_case=True), "iPhone_Case")

    def test_default_lowercases(self):
        self.assertEqual(slugify("iPhone Case"), "iphone_case")
        self.assertEqual(slugify("iPhone Case", keep_case=False), "iphone_case")

    def test_default_unchanged_for_existing_links(self):
        self.assertEqual(slugify("Hello, World!"), "hello_world")

    def test_keep_case_distinguishes_case(self):
        self.assertEqual(slugify("IPHONE", keep_case=True), "IPHONE")
        self.assertNotEqual(
            slugify("iPhone", keep_case=True), slugify("IPHONE", keep_case=True)
        )

    def test_keep_case_collapses_non_alphanumeric_runs(self):
        self.assertEqual(slugify("  Hello,  World!! ", keep_case=True), "Hello_World")

    def test_keep_case_with_max_length_and_separator(self):
        self.assertEqual(
            slugify("Hello big World", max_length=9, separator="-", keep_case=True),
            "Hello-big",
        )
        self.assertEqual(
            slugify("Supercalifragilistic", max_length=5, keep_case=True), "Super"
        )


class IsSlugTest(unittest.TestCase):
    def test_valid_slug(self):
        self.assertTrue(is_slug("hello_world"))

    def test_invalid_slugs(self):
        for text in ("Hello_World", "hello__world", "_hello", "", "hello-world"):
            with self.subTest(text=text):
                self.assertFalse(is_slug(text))

    def test_dash_separator(self):
        self.assertTrue(is_slug("hello-world", separator="-"))
        self.assertFalse(is_slug("hello_world", separator="-"))

    def test_invalid_separator_raises(self):
        for separator in ("ab", "a"):
            with self.subTest(separator=separator):
                with self.assertRaises(ValueError):
                    is_slug("x", separator=separator)


class UnslugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(unslugify("hello_world"), "Hello World")

    def test_empty_parts(self):
        self.assertEqual(unslugify("__a__b_"), "A B")

    def test_empty(self):
        self.assertEqual(unslugify(""), "")

    def test_reverse_of_slugify(self):
        self.assertEqual(unslugify(slugify("Hello World")), "Hello World")

    def test_dash_separator(self):
        self.assertEqual(unslugify("hello-world", separator="-"), "Hello World")

    def test_invalid_separator_raises(self):
        for separator in ("ab", "a"):
            with self.subTest(separator=separator):
                with self.assertRaises(ValueError):
                    unslugify("x", separator=separator)


if __name__ == "__main__":
    unittest.main()
