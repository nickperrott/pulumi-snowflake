import snowflake.connector


class SnowflakeConnectionProvider:
    """
    Returns a connection to a Snowflake database.
    """

    def __init__(self, username, password, accountName):
        self.username = username
        self.password = password
        self.accountName = accountName

    def get(self):
        return snowflake.connector.connect(
            user=self.username,
            password=self.password,
            account=self.accountName
        )
