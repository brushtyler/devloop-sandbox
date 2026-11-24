"""A tiny widget library, the test bed of devloop's installation guide."""


def slugify(text: str) -> str:
    """Lower-case words of ``text`` joined by single dashes."""
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    return "-".join(words)


def unslugify(slug: str) -> str:
    """Capitalised words of ``slug``, split on dashes, joined by single spaces."""
    return " ".join(part.capitalize() for part in slug.split("-") if part)
