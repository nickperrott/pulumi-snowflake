from pulumi.dynamic import CreateResult, DiffResult, ResourceProvider
from pulumi_snowflake.random_id import RandomId
from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.validation import Validation


class FileFormatProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake FileFormat resources
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__()
        self.connection_provider = connection_provider

    def create(self, inputs):
        connection = self.connection_provider.get()
        cursor = connection.cursor()

        # Snowflake's input binding only works for column values, not identifiers,
        # so we have to validate them manually and put straight into the SQL
        validated_database = Validation.validate_identifier(inputs["database"])
        validated_type = Validation.validate_identifier(inputs["type"])
        validated_name = self._get_validated_name(inputs)
        validated_schema = self._get_validated_schema_or_none(inputs)

        try:
            cursor.execute(f"USE DATABASE {validated_database}")

            if validated_schema is not None:
                cursor.execute(f"USE SCHEMA {validated_schema}")

            cursor.execute('\n'.join([
                f"CREATE FILE FORMAT {validated_name}",
                f"TYPE = {validated_type}"
            ]))
        finally:
            cursor.close()

        connection.close()

        return CreateResult(id_=validated_name, outs={
            "type": validated_type,
            "name": validated_name,
            "database": validated_database,
            "schema": validated_schema
        })

    def delete(self, id, props):
        connection = self.connection_provider.get()
        cursor = connection.cursor()

        validated_database = Validation.validate_identifier(props["database"])
        validated_id = Validation.validate_identifier(id)
        validated_schema = self._get_validated_schema_or_none(props)

        try:
            cursor.execute(f"USE DATABASE {validated_database}")

            if validated_schema is not None:
                cursor.execute(f"USE SCHEMA {validated_schema}")

            cursor.execute(f"DROP FILE FORMAT {validated_id}")
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

    def _get_validated_name(self, inputs):
        name = inputs.get("name")

        if name is None:
            name = f'{inputs["resource_name"]}_{RandomId.generate(7)}'

        return Validation.validate_identifier(name)

    def _get_validated_schema_or_none(self, inputs):
        schema = inputs.get("schema")

        if schema is not None:
            return Validation.validate_identifier(schema)

        return None
