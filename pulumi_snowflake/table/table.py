from typing import Optional, List

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource

from .column import Column
from .table_provider import TableProvider
from ..provider import Provider
from ..client import Client


class Table(Resource):
    """
    Represents a Snowflake Table.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/create-table.html
    for more details of parameters.
    """

    cluster_by: Output[Optional[List[str]]]
    """
    Specifies one or more columns or column expressions in the table as the clustering key.
    """

    data_retention_time_in_days: Output[Optional[int]]
    """
    Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed
    on historical data in the table. 
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the table.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 columns: Input[List[Column]],
                 database: Input[str] = None,
                 schema: Input[str] = None,
                 name: Input[Optional[str]] = None,
                 cluster_by: Output[Optional[List[str]]] = None,
                 data_retention_time_in_days: Output[Optional[int]] = None,
                 comment: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):
        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(TableProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'full_name': None,
            'columns': [column.as_dict() for column in columns],
            'database': database,
            'schema': schema,
            'name': name,
            'cluster_by': cluster_by,
            'data_retention_time_in_days': data_retention_time_in_days,
            'comment': comment
        }, opts)
