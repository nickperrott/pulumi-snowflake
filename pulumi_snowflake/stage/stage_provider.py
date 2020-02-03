from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.snowflakeprovider import StringAttribute, IdentifierAttribute
from pulumi_snowflake.snowflakeprovider.schema_scoped_object_provider import SchemaScopedObjectProvider
from pulumi_snowflake.snowflakeprovider.struct_attribute import StructAttribute


class StageProvider(SchemaScopedObjectProvider):
    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__(connection_provider, "STAGE", [
            StructAttribute("file_format", False, [
                StringAttribute("format_name", False),
                IdentifierAttribute("type", False)
            ]),
            StringAttribute("comment", False)
        ])


