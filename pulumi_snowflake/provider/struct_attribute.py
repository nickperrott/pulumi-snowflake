from typing import Tuple

from .base_attribute import BaseAttribute


class StructAttribute(BaseAttribute):

    def __init__(self, name: str, required: bool, fields):
        super().__init__(name, required)
        self.fields = fields

    def generate_sql(self, value) -> str:
        print("GENERATE")
        print(value)

        populated_fields = self.get_populated_fields(value)

        print("POP FIELDS")
        print(populated_fields)

        field_sql_statements = map(lambda f: self.generate_field_sql(value, f), populated_fields)

        print("DONE WITH SQL")

        field_sql_str = ", ".join(field_sql_statements)
        return f"{self.sql_name} = ({field_sql_str})"

    def generate_field_sql(self, value, attribute: BaseAttribute):
        print("DOING " + attribute.name)
        return attribute.generate_sql(value[attribute.name])

    def generate_bindings(self, value) -> Tuple:
        populated_fields = self.get_populated_fields(value)
        bindings = list(map(lambda f: f.generate_bindings(value[f.name]), populated_fields))
        bindings = list(filter(lambda b: b is not None, bindings))
        tuples = tuple(element for tupl in bindings for element in tupl)
        return tuples

    def generate_outputs(self, value):
        return { f.name: value[f.name] for f in self.fields }

    def check_required_fields(self, value):
        required_fields = filter(lambda f: f.is_required(), self.fields)

        for field in required_fields:
            if field.is_required() and value.get(field.name) is None:
                raise Exception(f"Required field {field.name} cannot be None")

    def get_populated_fields(self, value):
        self.check_required_fields(value)
        return list(filter(lambda f: value.get(f.name) is not None, self.fields))
