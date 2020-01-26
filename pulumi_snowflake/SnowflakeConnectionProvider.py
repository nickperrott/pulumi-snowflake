import snowflake.connector


class SnowflakeConnectionProvider:
    """
    Returns a connection to a Snowflake database.
    """

    def get(self, username, password, accountName):

        return snowflake.connector.connect(
            user=username,
            password=password,
            account=accountName
        )
