from pulumi.dynamic import CreateResult, ResourceProvider
from pulumi_snowflake.RandomId import RandomId
from pulumi_snowflake.SnowflakeConnectionProvider import \
    SnowflakeConnectionProvider
from pulumi_snowflake.Validation import Validation


class FileFormatProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake FileFormat resources
    """

    connectionProvider: SnowflakeConnectionProvider

    def __init__(self, connectionProvider: SnowflakeConnectionProvider):
        super().__init__()
        self.connectionProvider = connectionProvider

    def create(self, inputs):
        connection = self.connectionProvider.get()
        cursor = connection.cursor()

        # Snowflake's input binding only works for column values, not identifiers,
        # so we have to validate them manually and put straight into the SQL
        validatedDatabase = Validation.validateIdentifier(inputs["database"])
        validatedType = Validation.validateIdentifier(inputs["type"])
        validatedName = self._getValidatedName(inputs)
        validatedSchema = self._getValidatedSchemaOrNone(inputs)

        try:
            cursor.execute(f"USE DATABASE {validatedDatabase}")

            if validatedSchema is not None:
                cursor.execute(f"USE SCHEMA {validatedSchema}")

            cursor.execute('\n'.join([
                f"CREATE FILE FORMAT {validatedName}",
                f"TYPE = {validatedType}"
            ]))
        finally:
            cursor.close()

        connection.close()

        return CreateResult(id_=validatedName, outs={
            "type": validatedType,
            "name": validatedName,
            "database": validatedDatabase,
            "schema": validatedSchema
        })

    def delete(self, id, props):
        connection = self.connectionProvider.get()
        cursor = connection.cursor()

        validatedDatabase = Validation.validateIdentifier(props["database"])
        validatedId = Validation.validateIdentifier(id)
        validatedSchema = self._getValidatedSchemaOrNone(props)

        try:
            cursor.execute(f"USE DATABASE {validatedDatabase}")

            if validatedSchema is not None:
                cursor.execute(f"USE SCHEMA {validatedSchema}")

            cursor.execute(f"DROP FILE FORMAT {validatedId}")
        finally:
            cursor.close()

        connection.close()

    def _getValidatedName(self, inputs):
        name = inputs.get("name")

        if name is None:
            name = f'{inputs["resource_name"]}_{RandomId.generate(7)}'

        return Validation.validateIdentifier(name)

    def _getValidatedSchemaOrNone(self, inputs):
        schema = inputs.get("schema")

        if schema is not None:
            return Validation.validateIdentifier(schema)

        return None
