"""A tiny widget library, the test bed of devloop's installation guide."""


def slugify(text: str) -> str:
    """Lower-case words of ``text`` joined by single dashes."""
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    return "-".join(words)


def is_slug(text: str) -> bool:
    """True when ``text`` is non-empty and already its own slug."""
    return bool(text) and slugify(text) == text
