import re


class Validation:

    identifier_regex = re.compile("^[A-Za-z\\$\\_][A-Za-z0-9\\$\\_]+$")

    @staticmethod
    def validate_string(string: str, allow_none: bool = True):
        """ Validates a Snowflake string.  Strings can contain any character except single quotes, although
        single quotes may be escaped with a backslash.
        """
        if allow_none and string is None: return string

        pattern = re.compile("^(?:[^'\\\\]|\\\\.)*$")

        if not pattern.match(string):
            raise Exception(f'Invalid Snowflake string: {string}')

        return id

    @staticmethod
    def is_enquoted_identifier_valid(id: str):
        """
        Checks to see if the given identifier is valid even if it is enquoted in double quotes.  See
        https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
        """
        pattern = re.compile("^[\x20-\x21\x23-\x7E]*$") # Any printable character except double quote
        return pattern.match(id) is not None

    @staticmethod
    def enquote_identifier(id: str):
        """ Checks to see if the given identifier must be enclosed in double quotes, and if it does,
            returns the identifier with the quotes.
            https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
        """

        if id is None:
            return None
        elif Validation.identifier_regex.match(id):
            return id
        elif not Validation.is_enquoted_identifier_valid(id):
            raise Exception(f"Invalid identifier: {id}")
        else:
            return f'"{id}"'
