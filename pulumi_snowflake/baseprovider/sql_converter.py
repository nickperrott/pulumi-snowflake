from typing import Tuple


class SqlConverter:
    """
    This is a utility class which helps to convert Python values into Snowflake SQL values.
    """

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
            return SqlConverter.string_to_sql(value)
        elif isinstance(value, dict):
            return SqlConverter.dict_to_sql(value)
        elif isinstance(value, list):
            return SqlConverter.list_to_sql(value)
        elif isinstance(value, bool):
            return SqlConverter.bool_to_sql(value)
        elif isinstance(value, (int, float)):
            return SqlConverter.number_to_sql(value)
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
        values_and_bindings = list(map(lambda v: SqlConverter.generate_sql_value(v), value))
        all_values = list(map(lambda vb: vb[0], values_and_bindings))
        values_string = ",".join(all_values)
        return f"({values_string})"

    @staticmethod
    def dict_to_sql(value):
        valid_keys = filter(lambda k: value[k] is not None, value.keys())
        values_and_bindings = list(
            map(lambda k: SqlConverter.generate_key_value_sql_and_bindings(k, value[k]), valid_keys))
        all_values = list(map(lambda vb: vb[0], values_and_bindings))
        values_string = ", ".join(all_values)
        return f"({values_string})"

    @staticmethod
    def string_to_sql(value):
        # TODO: This needs to be validated to ensure it is a valid string (i.e. no single quotes except escaped ones)
        return f"'{value}'"

    @staticmethod
    def generate_key_value_sql_and_bindings(self, field_name, value) -> Tuple[str,Tuple]:
        if value is None:
            return ("", tuple())

        (sql_value,bindings) = self.generate_sql_value(value)
        sql = f"{field_name.upper()} = {sql_value}"
        return (sql,bindings)
