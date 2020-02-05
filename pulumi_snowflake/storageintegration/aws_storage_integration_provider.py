from pulumi_snowflake import ConnectionProvider
from ..provider.attribute.identifier_attribute import IdentifierAttribute
from ..provider.attribute.string_attribute import StringAttribute
from ..provider.attribute.boolean_attribute import BooleanAttribute
from ..provider.attribute.string_list_attribute import StringListAttribute
from ..provider.provider import Provider


class AWSStorageIntegrationProvider(Provider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "STORAGE INTEGRATION", [
            IdentifierAttribute("type", True),
            IdentifierAttribute("storage_provider", True),
            StringAttribute("storage_aws_role_arn", True),
            BooleanAttribute("enabled", True),
            StringListAttribute("storage_allowed_locations", True),
            StringListAttribute("storage_blocked_locations", False),
            StringAttribute("comment", False)
        ])
