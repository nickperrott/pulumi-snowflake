from ..connection_provider import ConnectionProvider
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider
from pulumi_snowflake.validation import Validation


class FileFormatProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake FileFormat resources.
    """

    connection_provider: ConnectionProvider

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "FILE FORMAT", [
            KeyValueAttribute("type"),
            KeyValueAttribute("comment")
        ])
