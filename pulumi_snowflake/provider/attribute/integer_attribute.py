from typing import Tuple

from .base_attribute import BaseAttribute
from ...validation import Validation


class IntegerAttribute(BaseAttribute):
    """
    Represents a integer SQL attribute.  Values are Python ints.
    """

    def __init__(self, name: str, required: bool = False):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        self.validate_int(value)
        return f"{self.sql_name} = {value}"

    def generate_bindings(self, value) -> Tuple:
        self.validate_int(value)
        return None

    def validate_int(self, value):
        if not isinstance(value, int):
            raise Exception("Argument to `IntegerAttribute` must be an integer")

        valueAsString = str(value)
        Validation.validate_integer(valueAsString)

