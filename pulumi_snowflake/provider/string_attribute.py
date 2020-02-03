from typing import Tuple

from .base_attribute import BaseAttribute

class StringAttribute(BaseAttribute):
    """
    Represents a string SQL attribute.  Values are Python strings.  The generated SQL will represent values with a
    `%s` placeholder for value binding, and returns the actual string value in `generate_bindings`.
    """

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        return f"{self.sql_name} = %s"

    def generate_bindings(self, value) -> Tuple:
        return (value,)
