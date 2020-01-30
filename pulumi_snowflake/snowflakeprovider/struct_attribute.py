from typing import Tuple

from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute


class StructAttribute(SnowflakeObjectAttribute):

    def __init__(self, name: str, required: bool, fields):
        super().__init__(name, required)
        self.fields = fields

    def generate_sql(self, value) -> str:
        field_sql_statements = map(lambda f: self.generate_field_sql(value, f), self.fields)
        field_sql_str = ", ".join(field_sql_statements)
        return f"{self.sql_name} = ({field_sql_str})"

    def generate_field_sql(self, value, attribute: SnowflakeObjectAttribute):
        return attribute.generate_sql(getattr(value, attribute.name))

    def generate_bindings(self, value) -> Tuple:
        bindings = list(map(lambda f: f.generate_bindings(getattr(value, f.name) ), self.fields))
        bindings = list(filter(lambda b: b is not None, bindings))
        tuples = tuple(element for tupl in bindings for element in tupl)
        return tuples

    def generate_outputs(self, value):
        return { f.name: getattr(value, f.name) for f in self.fields }

