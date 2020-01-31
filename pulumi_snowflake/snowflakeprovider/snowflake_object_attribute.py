from abc import ABC, abstractmethod
from typing import Tuple

from pulumi_snowflake.validation import Validation


class SnowflakeObjectAttribute(ABC):
    """
    Base class for SQL object attributes.  The subclasses of this class are used to define the attributes of a SQL
    object (e.g. Table, Schema, Storage Integration, etc.).

    The `generate_sql` method should return a single segment of SQL which sets the attribute to the given value using
    appropriate SQL syntax; for example, `TYPE = CSV` or `NAMES = (%s, %s)`.

    The `generate_bindings` method should return a tuple of values which should be bound to placeholders (`%s`) which
    were used in the SQL string.  For example, `('name1','name2')`.
    """

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
