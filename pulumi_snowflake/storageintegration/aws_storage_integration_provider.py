from pulumi_snowflake import ConnectionProvider
from pulumi_snowflake.provider import IdentifierAttribute, StringAttribute, BooleanAttribute, StringListAttribute, Provider


class AWSStorageIntegrationProvider(Provider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    connection_provider: ConnectionProvider

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "STORAGE INTEGRATION", [
            IdentifierAttribute("type", True),
            IdentifierAttribute("storage_provider", True),
            StringAttribute("storage_aws_role_arn", True),
            BooleanAttribute("enabled", True),
            StringListAttribute("storage_allowed_locations", True),
            StringListAttribute("storage_blocked_locations", False),
            StringAttribute("comment", False)
        ])
