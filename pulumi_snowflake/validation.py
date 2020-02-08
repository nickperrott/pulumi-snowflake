import re


class Validation:

    identifier_regex = re.compile("^[A-Za-z\\$\\_][A-Za-z0-9\\$\\_]+$")

    @staticmethod
    def validate_field_name(id: str):
        """ Validates a Snowflake resource name (e.g. DATA_RETENTION_TIME_IN_DAYS)
        """
        if not Validation.identifier_regex.match(id):
            raise Exception(f'Invalid Snowflake resource type name: {id}')

        return id

    @staticmethod
    def validate_object_type(id: str):
        """ Validates a Snowflake SQL object name, e.g. "FILE FORMAT"
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
