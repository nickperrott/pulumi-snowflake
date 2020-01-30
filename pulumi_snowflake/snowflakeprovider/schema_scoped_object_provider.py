from pulumi_snowflake.snowflakeprovider.snowflake_object_provider import SnowflakeObjectProvider
from pulumi_snowflake.validation import Validation


class SchemaScopedObjectProvider(SnowflakeObjectProvider):
    """
    A Pulumi dynamic provider which manages a Snowflake object which is scoped to a specific
     Schema (i.e., in contrast to globally scoped objects which exist at the account level).  Objects are described by
     passing in the SQL name of the object (e.g., "STORAGE INTEGRATION) and a list of attributes represented as
     `SnowflakeObjectAttribute` instances.  This class then automatically handles the create, delete and diff methods by
     generating and executing the appropriate SQL commands.
    """

    def generate_outputs(self, name, inputs, outs):
        """
        Appends the schema name and database name to the outputs
        """
        return {
            "database": inputs["database"],
            "schema": inputs.get("schema"),
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
