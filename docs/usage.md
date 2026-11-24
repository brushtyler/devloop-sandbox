# Usage

`widget.slugify(text)` returns the lower-case words of `text` joined by single dashes.

`widget.unslugify(slug)` is the reverse: it splits `slug` on dashes, drops empty parts,
capitalises each word and joins them with single spaces, so `unslugify("hello-world")`
returns `"Hello World"`.
