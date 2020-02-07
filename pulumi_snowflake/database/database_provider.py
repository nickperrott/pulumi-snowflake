from pulumi_snowflake import ConnectionProvider
from pulumi_snowflake.provider import Provider


class DatabaseProvider(Provider):
    """
    Dynamic provider for Snowflake Database resources.
    """

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "DATABASE", [

        ])

