from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute


class StringListAttribute(SnowflakeObjectAttribute):

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        placeholder = ','.join(['%s'] * len(value))
        return f"{self.sqlName} = ({placeholder})"

    def generate_bindings(self, value) -> Tuple:
        return (*value,)