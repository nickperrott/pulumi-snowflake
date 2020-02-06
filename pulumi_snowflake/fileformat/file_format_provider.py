from pulumi_snowflake import ConnectionProvider
from ..provider.attribute.key_value_attribute import KeyValueAttribute
from ..provider.provider import Provider
from pulumi_snowflake.validation import Validation


class FileFormatProvider(Provider):
    """
    Dynamic provider for Snowflake FileFormat resources.
    """

    connection_provider: ConnectionProvider

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "FILE FORMAT", [
            KeyValueAttribute("type"),
            KeyValueAttribute("comment")
        ])


    def generate_outputs(self, name, inputs, outs):
        """
        Appends the schema name and database name to the outputs
        """
        return {
            "database": inputs["database"],
            "schema": inputs.get("schema"),
            "full_name": self.get_full_object_name(name, inputs),
            **outs
        }

    def get_full_object_name(self, validated_name, inputs):
        """
        For objects which are scoped to a schema, the full qualified object name is in the form 'database.schema.name',
        where schema can be empty if the default schema is required.
        """
        validated_database = Validation.validate_identifier(inputs["database"])
        validated_schema = self._get_validated_schema_or_none(inputs)

        return f"{validated_database}.{validated_schema}.{validated_name}" \
            if validated_schema is not None else \
            f"{validated_database}..{validated_name}"

    def _get_validated_schema_or_none(self, inputs):
        schema = inputs.get("schema")

        if schema is not None:
            return Validation.validate_identifier(schema)

        return None
