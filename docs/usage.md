# Usage

`widget.slugify(text, max_length=None, separator="_")` returns the lower-case words of `text`
joined by single `separator` characters: `slugify("Hello, World!")` is `"hello_world"`, and
`slugify("Hello, World!", separator="-")` is `"hello-world"`.

> **Note:** the default separator changed from a dash (`-`) to an underscore (`_`), so slugs
> can be used as identifiers. Callers that want dashes pass `separator="-"`.

`separator` must be a single non-alphanumeric character (for example `_`, `-` or `.`); anything
else, such as `"ab"`, `"a"` or `""`, raises `ValueError`. `is_slug` and `unslugify` take the
same `separator` keyword argument, with the same default and the same check.

`max_length` bounds the length of the slug, separators included:

- `None` (the default): no limit.
- A positive integer: the slug is at most `max_length` characters long. Whole words are dropped
  from the end until it fits, so it never ends with a separator or a half word
  (`slugify("Hello big world", max_length=8)` is `"hello"`, and
  `slugify("Hello big world", max_length=9, separator=".")` is `"hello.big"`). If the first word
  alone is longer than `max_length`, the slug is its first `max_length` characters
  (`slugify("Supercalifragilistic", max_length=5)` is `"super"`).
- Lower than 1: raises `ValueError`.

`widget.is_slug(text, separator="_")` returns `True` when `text` is non-empty and already a slug
with that separator, that is `slugify(text, separator=separator) == text`, and `False` otherwise.
For example `is_slug("hello_world")` is `True`, while `is_slug("Hello_World")`,
`is_slug("hello__world")`, `is_slug("_hello")`, `is_slug("")` and `is_slug("hello-world")` are
`False`; `is_slug("hello-world", separator="-")` is `True`.

`widget.unslugify(slug, separator="_")` is the reverse of `slugify` with the same separator: it
splits `slug` on `separator`, drops empty parts, capitalises each word and joins them with single
spaces, so `unslugify("hello_world")` and `unslugify("hello-world", separator="-")` both return
`"Hello World"`.
