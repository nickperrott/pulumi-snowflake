from typing import Tuple

from .base_attribute import BaseAttribute
from ... import NoneValue


class ValueOrNoneAttribute(BaseAttribute):
    """
    Represents a SQL attribute which can take some value, or the special value NONE.  The value NONE should be
    represented by an instance of the `NoneType` class rather than Python `None`, as this indicates a lack of value.
    This class is a decorator which wraps another `BaseAttribute` instance which provides the actual value if NONE is
    not given.
    """

    def __init__(self, attribute: BaseAttribute):
        super().__init__(attribute.name, attribute.required)
        self.attribute = attribute

    def generate_sql(self, value) -> str:
        if value == NoneValue():
            return f"{self.sql_name} = NONE"
        else:
            return self.attribute.generate_sql(value)

    def generate_bindings(self, value) -> Tuple:
        if value == NoneValue():
            return None
        else:
            return self.attribute.generate_bindings(value)
