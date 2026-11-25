"""A tiny widget library, the test bed of devloop's installation guide."""


def slugify(text: str, max_length: int | None = None) -> str:
    """Lower-case words of ``text`` joined by single dashes.

    With ``max_length``, the slug is at most that many characters long: whole
    words are dropped from the end until it fits, and a first word longer than
    ``max_length`` is cut to its first ``max_length`` characters.
    """
    if max_length is not None and max_length < 1:
        raise ValueError("max_length must be at least 1")
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    slug = "-".join(words)
    if max_length is None or len(slug) <= max_length:
        return slug
    if len(words[0]) > max_length:
        return words[0][:max_length]
    while len(slug) > max_length:
        words.pop()
        slug = "-".join(words)
    return slug


def is_slug(text: str) -> bool:
    """True when ``text`` is non-empty and already its own slug."""
    return bool(text) and slugify(text) == text


def unslugify(slug: str) -> str:
    """Capitalised words of ``slug``, split on dashes, joined by single spaces."""
    return " ".join(part.capitalize() for part in slug.split("-") if part)
