from typing import Tuple

from jinja2 import Environment


class JinjaEnvironment:
    """
    Utility class for creating a Jinja environment which adds additional filters for SQL conversion.  The filters
    are:

        sql             Converts a value automatically to a Snowflake SQL string depending on its type, including
                         strings, ints, floats, bools, lists and dicts.
        sql_identifier  Converts a value to a Snowflake identifier.
    """

    @staticmethod
    def create():
        """
        Returns a new instance of the Jinja environment.
        """
        environment = Environment()
        environment.filters["sql"] = JinjaEnvironment.to_sql
        environment.filters["sql_identifier"] = JinjaEnvironment.to_identifier
        return environment

    @staticmethod
    def create_template(source: str):
        """
        Convenience method which creates a Jinja template based on the given string.
        """
        return JinjaEnvironment.create().from_string(source)

    @staticmethod
    def to_identifier(value):
        #TODO: will check if valid identifier and put double quotes around if necessary
        return value


    @staticmethod
    def to_sql(value, allow_none=True):
        """
        Converts a Python value to the appropriate SQL representation.  This method assumes that all Python strings
        are to be represented as Snowflake strings (i.e. single quoted) - to convert to an identifier, use the
        `to_identifier` method.
        """

        if allow_none and value is None:
            return None
        elif isinstance(value, str):
            return JinjaEnvironment.string_to_sql(value)
        elif isinstance(value, dict):
            return JinjaEnvironment.dict_to_sql(value)
        elif isinstance(value, list):
            return JinjaEnvironment.list_to_sql(value)
        elif isinstance(value, bool):
            return JinjaEnvironment.bool_to_sql(value)
        elif isinstance(value, (int, float)):
            return JinjaEnvironment.number_to_sql(value)
        else:
            raise Exception(f"Cannot convert type '{type(value)}' to SQL representation")

    @staticmethod
    def number_to_sql(value):
        if int(value) == value:
            value = int(value)
        return f"{value}"

    @staticmethod
    def bool_to_sql(value):
        return "TRUE" if value else "FALSE"

    @staticmethod
    def list_to_sql(value):
        all_values = list(map(lambda v: JinjaEnvironment.to_sql(v), value))
        values_string = ",".join(all_values)
        return f"({values_string})"

    @staticmethod
    def dict_to_sql(value):
        valid_keys = list(filter(lambda k: value[k] is not None, value.keys()))
        sql_values = {k: JinjaEnvironment.to_sql(value[k]) for k in valid_keys}
        sql_statements = [ f"{key.upper()} = {sql_values[key]}" for key in valid_keys ]
        values_string = ",".join(sql_statements)
        return f"({values_string})"

    @staticmethod
    def string_to_sql(value):
        # TODO: This needs to be validated to ensure it is a valid string (i.e. no single quotes except escaped ones)
        return f"'{value}'"

    @staticmethod
    def generate_key_value_sql_and_bindings(field_name, value) -> Tuple[str,Tuple]:
        if value is None:
            return ("", tuple())

        (sql_value,bindings) = JinjaEnvironment.to_sql(value)
        sql = f"{field_name.upper()} = {sql_value}"
        return (sql,bindings)
