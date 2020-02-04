from typing import Tuple

from .base_attribute import BaseAttribute


class StringListAttribute(BaseAttribute):
    """
    Represents a string list SQL attribute.  Values are Python lists of strings.  The generated SQL produces
    a comma-separated list in parentheses.  The list contains only `%s` placeholders, with the actual values being
    returned as binding values.
    """

    def __init__(self, name: str, required: bool = False):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        placeholder = ','.join(['%s'] * len(value))
        return f"{self.sql_name} = ({placeholder})"

    def generate_bindings(self, value) -> Tuple:
        return (*value,)