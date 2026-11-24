# Usage

`widget.slugify(text, max_length=None)` returns the lower-case words of `text` joined by single dashes.

`max_length` bounds the length of the slug:

- `None` (the default): no limit.
- A positive integer: the slug is at most `max_length` characters long. Whole words are dropped
  from the end until it fits, so it never ends with a dash or a half word
  (`slugify("Hello big world", max_length=8)` is `"hello"`). If the first word alone is longer
  than `max_length`, the slug is its first `max_length` characters
  (`slugify("Supercalifragilistic", max_length=5)` is `"super"`).
- Lower than 1: raises `ValueError`.
