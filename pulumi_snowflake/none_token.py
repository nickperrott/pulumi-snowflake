from pulumi_snowflake.provider.attribute.value_or_token_attribute import Token


class NoneToken(Token):
    """
    Represents the value NONE in SQL expressions.  Used by fields which can accept either a value or NONE.  Note that
    this is distinct from fields which have the Python value `None`, as this indicates a non-present field.
    """
    def __init__(self):
        super().__init__("NONE")
