import re


class Validation:

    @staticmethod
    def validate_identifier(id: str):
        """ Validates a Snowflake identifier.  See
            https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
        """
        pattern = re.compile("^([A-Z,a-z,0-9$_%])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake identifier: {id}')

        return id

    def validate_object_name(id: str):
        """ Validates a Snowflake SQL object name.
        """
        pattern = re.compile("^([A-Z,a-z,0-9$_ ])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake object name: {id}')

        return id

    @staticmethod
    def validate_integer(id: str):
        """ Validates an integer string.
        """
        pattern = re.compile("^([0-9])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake integer: {id}')

        return id
