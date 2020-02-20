import re


class Validation:

    @staticmethod
    def validate_identifier(id: str, allow_none: bool = True):
        """ Validates a Snowflake identifier.  See
            https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
        """
        if allow_none and id is None: return id

        pattern = re.compile("^([A-Z,a-z,0-9$_%])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake identifier: {id}')

        return id

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
    def validate_object_type(id: str):
        """ Validates a Snowflake SQL object name.
        """
        pattern = re.compile("^([A-Z,a-z,0-9$_ ])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake object type: {id}')

        return id


    @staticmethod
    def validate_qualified_object_name(id: str):
        """ Validates a Snowflake SQL object name.
        """
        pattern = re.compile("^([A-Z,a-z,0-9$_\\.])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake qualified object name: {id}')

        return id

    @staticmethod
    def validate_integer(id: str):
        """ Validates an integer string.
        """
        pattern = re.compile("^([0-9])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake integer: {id}')

        return id
