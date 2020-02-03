from typing import Tuple

from .base_attribute import BaseAttribute


class BooleanAttribute(BaseAttribute):
    """
    Represents a boolean SQL attribute.  Values are Python `bool`s which are converted to the SQL `TRUE` or `FALSE`.
    """

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        sqlValue = self._bool_to_sql(value)
        return f"{self.sql_name} = {sqlValue}"

    def generate_bindings(self, value) -> Tuple:
        return None

    def _bool_to_sql(self, value):
        if value is None:
            raise Exception("Cannot convert None value to SQL Boolean")

        return 'TRUE' if value else 'FALSE'