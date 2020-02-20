from typing import Optional

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from ..provider import Provider
from ..client import Client
from .database_provider import DatabaseProvider


class Database(Resource):
    """
    Represents a Snowflake Database.  See https://docs.snowflake.net/manuals/sql-reference/sql/create-database.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the database in Snowflake.
    """

    transient: Output[Optional[bool]]
    """
    Specifies a database as transient.
    """

    data_retention_time_in_days: Output[Optional[int]]
    """
    Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database.
    """

    share: Output[Optional[str]]
    """
    The name of a share from which this database is created.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the database.
    """


    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 comment: Input[Optional[str]] = None,
                 transient: Input[Optional[bool]] = None,
                 data_retention_time_in_days: Input[Optional[int]] = None,
                 share: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        connection_provider = Client(provider=provider)
        super().__init__(DatabaseProvider(provider, connection_provider), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'share': share,
            'transient': transient,
            'data_retention_time_in_days': data_retention_time_in_days,
            'comment': comment
        }, opts)
