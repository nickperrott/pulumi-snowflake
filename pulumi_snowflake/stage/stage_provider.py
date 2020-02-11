from ..connection_provider import ConnectionProvider
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class StageProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Stage resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "STAGE", [
            KeyValueAttribute("url"),
            KeyValueAttribute("storage_integration"),
            KeyValueAttribute("credentials"),
            KeyValueAttribute("encryption"),
            KeyValueAttribute("file_format"),
            KeyValueAttribute("copy_options"),
            KeyValueAttribute("comment")
        ],
        [
            "temporary"
        ])
