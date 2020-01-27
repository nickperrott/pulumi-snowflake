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

        name = inputs.get("name")

        if name is None:
            name = f'{inputs["resource_name"]}_{RandomId.generate(7)}'

        # Snowflake's input binding only works for column values, not identifiers,
        # so we have to validate them manually and put straight into the SQL
        validatedDatabase = Validation.validateIdentifier(inputs["database"])
        validatedName = Validation.validateIdentifier(name)
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

        return CreateResult(id_=validatedDatabase, outs={
            "type": validatedType,
            "name": validatedName
        })

    def delete(self, id, props):

        print("THE ID is")
        print(id)
        print("TJHE PROPS ARE")
        print(props)