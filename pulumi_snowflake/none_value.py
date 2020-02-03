class NoneValue:
    """
    Represents the value NONE in SQL expressions.  Used by fields which can accept either a value or NONE.  Note that
    this is distinct from fields which have the Python value `None`, as this indicates a non-present field.
    """
    pass

def eq_is_none(self, other):
    return isinstance(other, NoneValue)

NoneValue.__eq__ = eq_is_none
