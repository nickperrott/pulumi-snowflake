from pulumi import Input

from typing import Optional

class Column:
    """
    Represents a column in a Snowflake table.  Used by the `Table` resource constructor.
    """

    def __init__(self,
                 name: Input[Optional[str]],
                 type: Input[Optional[str]],
                 collation: Input[Optional[str]] = None,
                 default: Input[Optional[str]] = None,
                 autoincrement: Input[Optional[bool]] = None,
                 not_null: Input[Optional[bool]] = None,
                 unique: Input[Optional[bool]] = None,
                 primary_key: Input[Optional[bool]] = None
                 ):
        self.dict = {
            "name": name,
            "type": type,
            "collation": collation,
            "default": default,
            "autoincrement": autoincrement,
            "not_null": not_null,
            "unique": unique,
            "primary_key": primary_key,
        }

    def as_dict(self):
        return self.dict
