from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute

class StringAttribute(SnowflakeObjectAttribute):
    """
    Represents a string SQL attribute.  Values are Python strings.  The generated SQL will represent values with a
    `%s` placeholder for value binding, and returns the actual string value in `generate_bindings`.
    """

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        return f"{self.sqlName} = %s"

    def generate_bindings(self, value) -> Tuple:
        return (value,)
