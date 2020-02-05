from .token import Token


class UTF8Token(Token):
    """
    Represents the value UTF8 in SQL expressions.  Used by fields which can accept either a string value or UTF8, such
    as the `encoding` field in file format options.
    """
    def __init__(self):
        super().__init__("UTF8")
