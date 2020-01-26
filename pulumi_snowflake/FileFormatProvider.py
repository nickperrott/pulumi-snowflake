from pulumi.dynamic import CreateResult, ResourceProvider
from pulumi_snowflake.SnowflakeConnectionProvider import \
    SnowflakeConnectionProvider
from pulumi_snowflake.Validation import Validation


class FileFormatProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake FileFormat resources
    """

    connectionProvider: SnowflakeConnectionProvider

    def __init__(self, connectionProvider: SnowflakeConnectionProvider = None):
        super().__init__()

        if connectionProvider is None:
            self.connectionProvider = SnowflakeConnectionProvider()
        else:
            self.connectionProvider = connectionProvider

    def create(self, inputs):

        connection = self.connectionProvider.get(
            username=inputs["snowflakeUsername"],
            password=inputs["snowflakePassword"],
            accountName=inputs["snowflakeAccountName"]
        )
        cursor = connection.cursor()

        # Snowflake's input binding only works for column values, not identifiers,
        # so we have to validate them manually and put straight into the SQL
        validatedDatabase = Validation.validateIdentifier(inputs["database"])
        validatedName = Validation.validateIdentifier(inputs["name"])
        validatedType = Validation.validateIdentifier(inputs["type"])

        try:
            cursor.execute(f"USE DATABASE {validatedDatabase}")
            cursor.execute('\n'.join([
                f"CREATE FILE FORMAT {validatedName}",
                f"TYPE = {validatedType}"
            ]))
        finally:
            cursor.close()

        connection.close()

        return CreateResult(id_="foo", outs={
            "type": validatedType,
            "name": validatedName
        })
