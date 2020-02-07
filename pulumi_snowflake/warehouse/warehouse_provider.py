from pulumi_snowflake import ConnectionProvider

from ..baseprovider import BaseDynamicProvider, KeyValueAttribute
from ..provider import Provider


class WarehouseProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Warehouse resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "WAREHOUSE", [
            KeyValueAttribute("warehouse_size"),
            KeyValueAttribute("max_cluster_count"),
            KeyValueAttribute("min_cluster_count"),
            KeyValueAttribute("scaling_policy"),
            KeyValueAttribute("auto_suspend"),
            KeyValueAttribute("auto_resume"),
            KeyValueAttribute("initially_suspended"),
            KeyValueAttribute("resource_monitor"),
            KeyValueAttribute("comment")
        ])
