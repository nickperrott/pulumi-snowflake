from typing import Tuple

from .base_attribute import BaseAttribute
from pulumi_snowflake.validation import Validation

class IdentifierAttribute(BaseAttribute):
    """
    Represents an attribute which holds a SQL identifier.  Identifiers may contain alphanumeric characters and
    underscores only.  Values are Python strings which are converted to the SQL identifiers (i.e. strings without
    quotes).
    """

    def __init__(self, name: str, required: bool = False):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        Validation.validate_identifier(value)
        return f"{self.sql_name} = {value}"

    def generate_bindings(self, value) -> Tuple:
        return None
