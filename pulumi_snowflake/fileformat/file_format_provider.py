from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.snowflakeprovider import IdentifierAttribute
from pulumi_snowflake.snowflakeprovider.schema_scoped_object_provider import SchemaScopedObjectProvider


class FileFormatProvider(SchemaScopedObjectProvider):
    """
    Dynamic provider for Snowflake FileFormat resources.
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__(connection_provider, "FILE FORMAT", [
            IdentifierAttribute("type", True),
            # StringAttribute("comment", False)
        ])
