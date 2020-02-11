from ..connection_provider import ConnectionProvider
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class AWSStorageIntegrationProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "STORAGE INTEGRATION", [
            KeyValueAttribute("type"),
            KeyValueAttribute("storage_provider"),
            KeyValueAttribute("storage_aws_role_arn"),
            KeyValueAttribute("enabled"),
            KeyValueAttribute("storage_allowed_locations"),
            KeyValueAttribute("storage_blocked_locations"),
            KeyValueAttribute("comment"),
        ])
