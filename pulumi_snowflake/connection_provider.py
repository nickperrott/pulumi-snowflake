import snowflake.connector


class ConnectionProvider:
    """
    Returns a connection to a Snowflake database.
    """

    def __init__(self, credentials):
        self.credentials = credentials

    def get(self):
        return snowflake.connector.connect(
            user=self.credentials.username,
            password=self.credentials.password,
            account=self.credentials.account_name,
            role=self.credentials.role
        )