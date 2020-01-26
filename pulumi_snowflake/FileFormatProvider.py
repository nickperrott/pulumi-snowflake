from pulumi.dynamic import CreateResult, ResourceProvider
from pulumi_snowflake.SnowflakeConnectionProvider import SnowflakeConnectionProvider


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

        version = "novalue"

        try:
            cursor.execute("SELECT current_version()")
            one_row = cursor.fetchone()
            version = f"{one_row[0]}"
            print(version)
        finally:
            cursor.close()

        connection.close()

        return CreateResult(id_="foo", outs={
            "name": version
        })
