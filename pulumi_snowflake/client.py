import snowflake.connector

from .provider import Provider


class Client:
    """
    Returns a connection to a Snowflake database.
    """

    def __init__(self, provider: Provider):
        """
        :param provider: The Snowflake provider parameters
        """
        self.provider = provider

    def get(self):
        return snowflake.connector.connect(
            user=self.provider.username,
            password=self.provider.password,
            account=self.provider.account_name,
            role=self.provider.role,
            database=self.provider.database,
            schema=self.provider.schema
        )