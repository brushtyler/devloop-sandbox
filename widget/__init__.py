"""A tiny widget library, the test bed of devloop's installation guide."""


def _check_separator(separator: str) -> None:
    """Raise ``ValueError`` unless ``separator`` is one non-alphanumeric character."""
    if not isinstance(separator, str) or len(separator) != 1 or separator.isalnum():
        raise ValueError("separator must be a single non-alphanumeric character")


def slugify(
    text: str,
    max_length: int | None = None,
    separator: str = "_",
    keep_case: bool = False,
) -> str:
    """Lower-case words of ``text`` joined by single ``separator`` characters.

    With ``keep_case=True`` every letter keeps its original case instead.

    ``separator`` must be a single non-alphanumeric character (``ValueError``
    otherwise); it defaults to an underscore.

    With ``max_length``, the slug is at most that many characters long,
    separators included: whole words are dropped from the end until it fits,
    and a first word longer than ``max_length`` is cut to its first
    ``max_length`` characters.
    """
    _check_separator(separator)
    if max_length is not None and max_length < 1:
        raise ValueError("max_length must be at least 1")
    words = "".join(
        (c if keep_case else c.lower()) if c.isalnum() else " " for c in text
    ).split()
    slug = separator.join(words)
    if max_length is None or len(slug) <= max_length:
        return slug
    if len(words[0]) > max_length:
        return words[0][:max_length]
    while len(slug) > max_length:
        words.pop()
        slug = separator.join(words)
    return slug


def is_slug(text: str, separator: str = "_") -> bool:
    """True when ``text`` is non-empty and already its own slug with ``separator``."""
    _check_separator(separator)
    return bool(text) and slugify(text, separator=separator) == text


def unslugify(slug: str, separator: str = "_") -> str:
    """Capitalised words of ``slug``, split on ``separator``, joined by single spaces."""
    _check_separator(separator)
    return " ".join(part.capitalize() for part in slug.split(separator) if part)
