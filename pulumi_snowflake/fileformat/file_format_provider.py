from typing import List

from pulumi.dynamic import CreateResult, DiffResult, ResourceProvider
from pulumi_snowflake.random_id import RandomId
from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.snowflakeprovider import IdentifierAttribute
from pulumi_snowflake.snowflakeprovider.schema_scoped_object_provider import SchemaScopedObjectProvider
from pulumi_snowflake.validation import Validation


class FileFormatProvider(SchemaScopedObjectProvider):
    """
    Dynamic provider for Snowflake FileFormat resources
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__(connection_provider, "FILE FORMAT", [
            IdentifierAttribute("type", True),
            # StringAttribute("comment", False)
        ])

    def delete(self, id, props):
        connection = self.connection_provider.get()
        cursor = connection.cursor()

        validated_database = Validation.validate_identifier(props["database"])
        validated_id = Validation.validate_identifier(id)
        validated_schema = self._get_validated_schema_or_none(props)
        qualified_name = self._get_qualified_object_name(validated_database, validated_id, validated_schema)

        try:
            cursor.execute(f"DROP FILE FORMAT {qualified_name}")
        finally:
            cursor.close()

        connection.close()

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

    def _get_validated_schema_or_none(self, inputs):
        schema = inputs.get("schema")

        if schema is not None:
            return Validation.validate_identifier(schema)

        return None

    def _get_qualified_object_name(self, validated_database, validated_name, validated_schema):
        qualifiedName = f"{validated_database}.{validated_schema}.{validated_name}" \
            if validated_schema is not None else \
            f"{validated_database}..{validated_name}"
        return qualifiedName
