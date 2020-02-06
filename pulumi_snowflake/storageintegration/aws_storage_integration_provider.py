from pulumi_snowflake import ConnectionProvider
from ..provider.attribute.key_value_attribute import KeyValueAttribute
from ..provider.provider import Provider


class AWSStorageIntegrationProvider(Provider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "STORAGE INTEGRATION", [
            KeyValueAttribute("type"),
            KeyValueAttribute("storage_provider"),
            KeyValueAttribute("storage_aws_role_arn"),
            KeyValueAttribute("enabled"),
            KeyValueAttribute("storage_allowed_locations"),
            KeyValueAttribute("storage_blocked_locations"),
            KeyValueAttribute("comment"),
        ])
