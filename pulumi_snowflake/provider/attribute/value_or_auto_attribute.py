from typing import Tuple

from .base_attribute import BaseAttribute
from ... import AutoValue


class ValueOrAutoAttribute(BaseAttribute):
    """
    Represents a SQL attribute which can take some value, or the special value AUTO.  The value AUTO should be
    represented by an instance of the `AutoType` class.  This class is a decorator which wraps another `BaseAttribute`
    instance which provides the actual value if AUTO is not given.
    """

    def __init__(self, attribute: BaseAttribute):
        super().__init__(attribute.name, attribute.required)
        self.attribute = attribute

    def generate_sql(self, value) -> str:
        if value == AutoValue():
            return f"{self.sql_name} = AUTO"
        else:
            return self.attribute.generate_sql(value)

    def generate_bindings(self, value) -> Tuple:
        if value == AutoValue():
            return None
        else:
            return self.attribute.generate_bindings(value)
