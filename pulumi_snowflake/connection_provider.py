import snowflake.connector
from pulumi import info

from .provider import Provider


class ConnectionProvider:
    """
    Returns a connection to a Snowflake database.
    """

    def __init__(self, provider: Provider):
        """
        :param provider: The Snowflake provider parameters
        """
        self.provider = provider

    def get(self):

        info(f"Creating Snowflake connection for account={self.provider.account_name} user={self.provider.username}"
             f"role={self.provider.role} database={self.provider.database} schema={self.provider.schema}")

        return snowflake.connector.connect(
            user=self.provider.username,
            password=self.provider.password,
            account=self.provider.account_name,
            role=self.provider.role,
            database=self.provider.database,
            schema=self.provider.schema
        )