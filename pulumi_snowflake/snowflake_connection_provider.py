import snowflake.connector


class SnowflakeConnectionProvider:
    """
    Returns a connection to a Snowflake database.
    """

    def __init__(self, username, password, account_name):
        self.username = username
        self.password = password
        self.account_name = account_name

    def get(self):
        return snowflake.connector.connect(
            user=self.username,
            password=self.password,
            account=self.account_name
        )
