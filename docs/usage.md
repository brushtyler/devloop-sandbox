# Usage

`widget.slugify(text)` returns the lower-case words of `text` joined by single dashes.

`widget.is_slug(text)` returns `True` when `text` is non-empty and already a slug, that is
`slugify(text) == text`, and `False` otherwise. For example `is_slug("hello-world")` is `True`,
while `is_slug("Hello-World")`, `is_slug("hello--world")`, `is_slug("-hello")` and `is_slug("")`
are `False`.
