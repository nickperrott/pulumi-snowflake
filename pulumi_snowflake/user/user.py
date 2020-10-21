from typing import Optional, List

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from .. import Client
from ..provider import Provider
from .user_provider import UserProvider


class User(Resource):
    """
    Represents a Snowflake User.  See https://docs.snowflake.com/en/sql-reference/sql/create-user.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the User in Snowflake.
    """

    password: Output[Optional[str]]
    """
    Specifies the initial password.   Normally we would use an RSA public key rather than a password.
    """

    login_name: Output[Optional[str]]
    display_name:  Output[Optional[str]]
    first_name:  Output[Optional[str]]
    middle_name:  Output[Optional[str]]
    last_name:  Output[Optional[str]]
    email:  Output[Optional[str]]
    must_change_password:  Output[bool]
    disabled: Output[bool]
    snowflake_support: Output[bool]
    days_to_expiry: Output[Optional[int]]
    mins_to_unlock: Output[Optional[int]]
    default_warehouse: Output[Optional[str]]

    default_namespace: Output[Optional[str]]
    default_User: Output[Optional[str]]
    default_warehouse: Output[Optional[str]]
    mins_to_bypass_mfa: Output[Optional[int]]
    rsa_public_key: Output[Optional[str]]
    rsa_public_key_2: Output[Optional[str]]

    network_policy: Output[Optional[str]]

    grant_roles: Output[Optional[List[str]]]

    comment: Output[Optional[str]]
    """
    Specifies a comment for the User.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 password: Output[Optional[str]] = None,
                 login_name: Output[Optional[str]] = None,
                 display_name:  Output[Optional[str]] = None,
                 first_name:  Output[Optional[str]] = None,
                 middle_name:  Output[Optional[str]] = None,
                 last_name:  Output[Optional[str]] = None,
                 email:  Output[Optional[str]] = None,
                 must_change_password:  Output[bool] = True,
                 disabled: Output[bool] = True,
                 days_to_expiry: Output[Optional[int]] = 30,
                 mins_to_unlock: Output[Optional[int]] = 0,
                 default_warehouse: Output[Optional[str]] = None,
                 default_namespace: Output[Optional[str]] = None,
                 default_role: Output[Optional[str]] = "Public",
                 mins_to_bypass_mfa: Output[Optional[int]] = 30,
                 rsa_public_key: Output[Optional[str]] = None,
                 rsa_public_key_2: Output[Optional[str]] = None,

                 network_policy: Output[Optional[str]] = None,
                 grant_roles: Output[Optional[List[str]]] = [],
                 provider: Provider = None,
                 comment: Input[Optional[str]] = None,
                 opts: Optional[ResourceOptions] = None):

        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(UserProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'full_name': None,
            'name': name,
            'password': password,
            'login_name': login_name,
            'display_name': display_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'email': email,
            'must_change_password': must_change_password,
            'disabled': disabled,
            'days_to_expiry': days_to_expiry,
            'mins_to_unlock': mins_to_unlock,
            'default_warehouse': default_warehouse,
            'default_namespace': default_namespace,
            'default_role': default_role,
            'mins_to_bypass_mfa': mins_to_bypass_mfa,
            'rsa_public_key': rsa_public_key,
            'rsa_public_key_2': rsa_public_key_2,
            'network_policy': network_policy,
            'grant_roles': grant_roles,
            'comment': comment
        }, opts)
