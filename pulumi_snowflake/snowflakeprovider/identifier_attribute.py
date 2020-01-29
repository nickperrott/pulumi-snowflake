from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute
from pulumi_snowflake.validation import Validation

class IdentifierAttribute(SnowflakeObjectAttribute):

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        Validation.validate_identifier(value)
        return f"{self.sqlName} = {value}"

    def generate_bindings(self, value) -> Tuple:
        return None
