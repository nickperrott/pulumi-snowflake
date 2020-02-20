from typing import Optional

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from .. import Client
from ..provider import Provider
from .schema_provider import SchemaProvider


class Schema(Resource):
    """
    Represents a Snowflake Schema.  See https://docs.snowflake.net/manuals/sql-reference/sql/create-schema.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the schema in Snowflake.
    """

    transient: Output[Optional[bool]]
    """
    Specifies a schema as transient.
    """

    data_retention_time_in_days: Output[Optional[int]]
    """
    Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema.
    """

    database: Output[Optional[str]]
    """
    Specifies a the database the schema belongs to.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the schema.
    """


    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 comment: Input[Optional[str]] = None,
                 transient: Input[Optional[bool]] = None,
                 data_retention_time_in_days: Input[Optional[int]] = None,
                 database: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(SchemaProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'transient': transient,
            'data_retention_time_in_days': data_retention_time_in_days,
            'database': database,
            'comment': comment
        }, opts)
