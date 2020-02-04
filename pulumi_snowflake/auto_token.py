from pulumi_snowflake.token import Token


class AutoToken(Token):
    """
    Represents the value AUTO in SQL expressions.  Used by fields which can accept either a value or AUTO.
    """
    def __init__(self):
        super().__init__("AUTO")
