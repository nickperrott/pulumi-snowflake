from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute


class BooleanAttribute(SnowflakeObjectAttribute):

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        sqlValue = self._bool_to_sql(value)
        return f"{self.sqlName} = {sqlValue}"

    def generate_bindings(self, value) -> Tuple:
        return None

    def _bool_to_sql(self, value):
        if value is None:
            raise Exception("Cannot convert None value to SQL Boolean")

        return 'TRUE' if value else 'FALSE'