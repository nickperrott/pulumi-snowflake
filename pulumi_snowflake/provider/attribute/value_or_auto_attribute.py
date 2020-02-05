from .base_attribute import BaseAttribute
from .value_or_token_attribute import ValueOrTokenAttribute
from ...auto_token import AutoToken


class ValueOrAutoAttribute(ValueOrTokenAttribute):
    """
    Represents a SQL attribute which can take some value, or the special value AUTO.  The value AUTO should be
    represented by an instance of the `AutoType` class.  This class is a decorator which wraps another `BaseAttribute`
    instance which provides the actual value if AUTO is not given.
    """
    def __init__(self, attribute: BaseAttribute):
        super().__init__(attribute, AutoToken())