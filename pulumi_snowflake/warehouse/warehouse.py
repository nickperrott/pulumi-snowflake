from typing import Optional, Union

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from ..provider import Provider
from ..connection_provider import ConnectionProvider
from .warehouse_provider import WarehouseProvider


class Warehouse(Resource):
    """
    Represents a Snowflake Warehouse.  See https://docs.snowflake.net/manuals/sql-reference/sql/create-warehouse.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the warehouse in Snowflake.
    """

    warehouse_size: Output[Optional[str]]
    """
    Specifies the size of the virtual warehouse.  Should be one of `WarehouseSizeValues`.
    """

    max_cluster_count: Output[Optional[int]]
    """
    Specifies the maximum number of server clusters for the warehouse.
    """

    min_cluster_count: Output[Optional[int]]
    """
    Specifies the minimum number of server clusters for the warehouse (only applies to multi-cluster warehouses).
    """

    scaling_policy: Output[Optional[str]]
    """
    Specifies the policy for automatically starting and shutting down clusters in a multi-cluster warehouse running in
    Auto-scale mode.  Should be one of `WarehouseScalingPolicyValues`.
    """

    auto_suspend: Output[Optional[Union[int,str]]]
    """
    Specifies the number of seconds of inactivity after which a warehouse is automatically suspended.
    """

    auto_resume: Output[Optional[bool]]
    """
    Specifies whether to automatically resume a warehouse when a SQL statement (e.g. query) is submitted to it.
    """

    initially_suspended: Output[Optional[bool]]
    """
    Specifies whether the warehouse is created initially in the ‘Suspended’ state.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the warehouse.
    """

    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 warehouse_size: Input[Optional[str]] = None,
                 max_cluster_count: Input[Optional[int]] = None,
                 min_cluster_count: Input[Optional[int]] = None,
                 scaling_policy: Input[Optional[str]] = None,
                 auto_suspend: Input[Optional[Union[int, str]]] = None,
                 auto_resume: Input[Optional[bool]] = None,
                 initially_suspended: Input[Optional[bool]] = None,
                 comment: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        connection_provider = ConnectionProvider(provider=provider)
        super().__init__(WarehouseProvider(provider, connection_provider), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'warehouse_size': warehouse_size,
            'max_cluster_count': max_cluster_count,
            'min_cluster_count': min_cluster_count,
            'scaling_policy': scaling_policy,
            'auto_suspend': auto_suspend,
            'auto_resume': auto_resume,
            'initially_suspended': initially_suspended,
            'comment': comment
        }, opts)
