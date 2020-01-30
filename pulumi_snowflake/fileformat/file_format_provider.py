from pulumi.dynamic import DiffResult
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

    def diff(self, id, olds, news):
        fields = ["type", "database", "schema"]
        changed_fields = []

        for field in fields:
            if olds.get(field) != news.get(field):
                changed_fields.append(field)

        if (news.get("name") is not None and olds.get("name") != news.get("name")):
            changed_fields.append("name")
        
        return DiffResult(
            changes=len(changed_fields) > 0,
            replaces=changed_fields
        )
