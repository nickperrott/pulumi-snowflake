from abc import ABC, abstractmethod
from typing import Tuple

from pulumi_snowflake.validation import Validation


class SnowflakeObjectAttribute(ABC):

    def __init__(self, name: str, required: bool):
        Validation.validate_identifier(name)
        self.name = name
        self.sqlName = name.upper()
        self.required = required

    def is_required(self) -> bool:
        return self.required

    @abstractmethod
    def generate_sql(self, value) -> str:
        pass

    @abstractmethod
    def generate_bindings(self, value) -> Tuple:
        pass

    def generate_outputs(self, value):
        return value

    def __repr__(self):
        return f"SnowflakeObjectAttribute({self.name},{self.required})"
