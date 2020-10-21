from typing import Optional, List

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from .. import Client
from ..provider import Provider
from .grant_provider import GrantProvider


class Grant(Resource):
    """
    Represents a Snowflake Role.  See https://docs.snowflake.com/en/sql-reference/sql/grant-privilege.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the role in Snowflake.
    """

    database: Output[str]
    """
    Specifies the database that the privileges will be granted on
    """

    privileges: Output[List[str]]
    """
    A list of database privileges as defined in the DatabasePrivelegeValues class.
    """

    role: Output[str]
    """
    The Snowflake role to grant the privileges to 
    """

    grant_option: Output[bool]
    """
    Set to true to include the grant option to the grant.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 database: Output[str] = None,
                 privileges: Output[List[str]] = [],
                 role: Output[str] = None,
                 grant_option: Input[bool] = False,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(GrantProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'full_name': None,
            'name': name,
            'database': database,
            'privileges': privileges,
            'role': role,
            'grant_option': grant_option
        }, opts)
