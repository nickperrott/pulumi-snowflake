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

    grant_on_type: Output[str]
    """
    Specifies the type of object that the grant is on.  i.e DATABASE | WAREHOUSE
    """

    grant_on: Output[str]
    """
    Specifies the name of the object tha the privileges will be granted on
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
                 grant_on_type: Output[str] = "DATABASE",
                 grant_on: Output[str] = None,
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
            'grant_on_type' : grant_on_type,
            'grant_on': grant_on,
            'privileges': privileges,
            'role': role,
            'grant_option': grant_option
        }, opts)
