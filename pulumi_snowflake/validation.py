import re


class Validation:

    @staticmethod
    def validate_identifier(id: str):
        """ Validates a Snowflake identifier.  See
            https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html
        """
        pattern = re.compile("^([A-Z,a-z,0-9$_])+$")

        if not pattern.match(id):
            raise Exception(f'Invalid Snowflake identifier: {id}')

        return id
