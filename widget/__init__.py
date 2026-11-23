"""A tiny widget library, the test bed of devloop's installation guide."""


def slugify(text: str) -> str:
    """Lower-case words of ``text`` joined by single dashes."""
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    return "-".join(words)
