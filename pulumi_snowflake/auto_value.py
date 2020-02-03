class AutoValue:
    """
    Represents the value AUTO in SQL expressions.  Used by fields which can accept either a value or AUTO.
    """
    pass

def eq_is_auto(self, other):
    return isinstance(other, AutoValue)

AutoValue.__eq__ = eq_is_auto
