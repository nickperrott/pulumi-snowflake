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

    def generate_sql_create_header(self, validated_name, inputs):
        """
        Returns the start of the SQL statement which creates an object using its fully qualified name (i.e.
        database.schema.name)
        """
        validated_database = Validation.validate_identifier(inputs["database"])
        validated_schema = self._get_validated_schema_or_none(inputs)
        qualified_name = self._get_qualified_object_name(validated_database, validated_name, validated_schema)

        return f"CREATE {self.sql_name} {qualified_name}"

    def generate_outputs(self, name, inputs, outs):
        """
        Appends the schema name and database name to the outputs
        """
        return {
            "database": inputs["database"],
            "schema": inputs.get("schema"),
            **outs
        }
