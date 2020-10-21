from typing import Optional

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from .. import Client
from ..provider import Provider
from .role_provider import RoleProvider


class Role(Resource):
    """
    Represents a Snowflake Role.  See https://docs.snowflake.com/en/sql-reference/sql/create-role.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the role in Snowflake.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the role.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 provider: Provider = None,
                 comment: Input[Optional[str]] = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(RoleProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'full_name': None,
            'name': name,
            'comment': comment
        }, opts)
