from typing import Optional

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from pulumi_snowflake import ConnectionProvider, Credentials
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

    data_retention_in_days: Output[Optional[int]]
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
                 share: Input[Optional[str]] = None,
                 opts: Optional[ResourceOptions] = None):
        connection_provider = ConnectionProvider(credentials=Credentials.create_from_config())
        super().__init__(DatabaseProvider(connection_provider), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'share': share,
            'transient': transient,
            'comment': comment
        }, opts)
