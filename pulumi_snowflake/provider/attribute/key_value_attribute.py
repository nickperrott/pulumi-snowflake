from typing import Tuple

from pulumi_snowflake.provider.attribute.base_attribute import BaseAttribute


class KeyValueAttribute(BaseAttribute):
    """
    Represents a key-value attribute as part of a SQL CREATE or UPDATE statement.  This class automatically converts
    values to the appropriate SQL type based on their Python type.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def generate_sql(self, value) -> str:
        return self.generate_sql_and_bindings(value)[0]

    def generate_bindings(self, value) -> Tuple:
        return self.generate_sql_and_bindings(value)[1]

    def generate_sql_and_bindings(self, value) -> Tuple[str, Tuple]:
        return self.generate_key_value_sql_and_bindings(self.sql_name, value)

    def generate_key_value_sql_and_bindings(self, field_name, value) -> Tuple[str,Tuple]:
        if value is None:
            return ("", tuple())

        (sql_value,bindings) = self.generate_sql_value(value)
        sql = f"{field_name.upper()} = {sql_value}"
        return (sql,bindings)

    def generate_sql_value(self, value) -> Tuple[str,Tuple]:
        """
        Converts a Python value to the appropriate SQL representation.  This method also returns any binding values,
        since strings are represented using the "%s" placeholder.
        """
        bindings = tuple()

        if isinstance(value, str):
            sql = "%s"
            bindings = (value,)
        elif isinstance(value, dict):
            valid_keys = filter(lambda k: value[k] is not None, value.keys())
            values_and_bindings = list(map(lambda k: self.generate_key_value_sql_and_bindings(k, value[k]), valid_keys))
            all_values = list(map(lambda vb: vb[0], values_and_bindings))
            all_bindings = list(map(lambda vb: vb[1], values_and_bindings))
            values_string = ", ".join(all_values)
            sql = f"({values_string})"
            bindings = tuple(i for sub in all_bindings for i in sub)

        elif isinstance(value, list):
            values_and_bindings = list(map(lambda v: self.generate_sql_value(v), value))
            all_values = list(map(lambda vb: vb[0], values_and_bindings))
            all_bindings = list(map(lambda vb: vb[1], values_and_bindings))
            values_string = ",".join(all_values)
            sql = f"({values_string})"
            bindings = tuple(i for sub in all_bindings for i in sub)

        elif isinstance(value, bool):
            sql = "TRUE" if value else "FALSE"
        elif isinstance(value, (int, float)):
            if int(value) == value:
                value = int(value)
            sql = f"{value}"
        else:
            raise Exception(f"Cannot convert type '{type(value)}' to SQL representation")

        return (sql,bindings)