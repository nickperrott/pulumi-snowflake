from .base_attribute import BaseAttribute
from .value_or_token_attribute import ValueOrTokenAttribute
from ... import NoneToken


class ValueOrNoneAttribute(ValueOrTokenAttribute):
    """
    Represents a SQL attribute which can take some value, or the special value NONE.  The value NONE should be
    represented by an instance of the `NoneType` class rather than Python `None`, as this indicates a lack of value.
    This class is a decorator which wraps another `BaseAttribute` instance which provides the actual value if NONE is
    not given.
    """

    def __init__(self, attribute: BaseAttribute):
        super().__init__(attribute, NoneToken())