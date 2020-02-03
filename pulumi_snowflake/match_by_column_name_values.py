class MatchByColumnNameValues:
    """
    Enum of possible methods for matching column name values when copying data.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html#copy-options-copyoptions for more details.
    """
    CASE_SENSITIVE = 'CASE_SENSITIVE'
    CASE_INSENSITIVE = 'CASE_INSENSITIVE'
    NONE = 'NONE'
