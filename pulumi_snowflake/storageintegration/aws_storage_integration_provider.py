from pulumi_snowflake.snowflake_connection_provider import SnowflakeConnectionProvider
from pulumi_snowflake.snowflakeprovider import IdentifierAttribute, StringAttribute
from pulumi_snowflake.snowflakeprovider.boolean_attribute import BooleanAttribute
from pulumi_snowflake.snowflakeprovider.provider import Provider
from pulumi_snowflake.snowflakeprovider.string_list_attribute import StringListAttribute


class AWSStorageIntegrationProvider(Provider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__(connection_provider, "STORAGE INTEGRATION", [
            IdentifierAttribute("type", True),
            IdentifierAttribute("storage_provider", True),
            StringAttribute("storage_aws_role_arn", True),
            BooleanAttribute("enabled", True),
            StringListAttribute("storage_allowed_locations", True),
            StringListAttribute("storage_blocked_locations", False),
            StringAttribute("comment", False)
        ])
