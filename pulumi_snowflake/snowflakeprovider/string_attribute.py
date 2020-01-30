from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute

class StringAttribute(SnowflakeObjectAttribute):

    def __init__(self, name: str, required: bool):
        super().__init__(name, required)

    def generate_sql(self, value) -> str:
        return f"{self.sql_name} = %s"

    def generate_bindings(self, value) -> Tuple:
        return (value,)
