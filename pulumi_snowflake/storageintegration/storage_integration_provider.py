from ..client import Client
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class StorageIntegrationProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, "STORAGE INTEGRATION", [
            KeyValueAttribute("type"),
            KeyValueAttribute("storage_provider"),
            KeyValueAttribute("storage_aws_role_arn"),
            KeyValueAttribute("enabled"),
            KeyValueAttribute("storage_allowed_locations"),
            KeyValueAttribute("storage_blocked_locations"),
            KeyValueAttribute("comment"),
        ])

    def _generate_sql_create_statement(self, attributesWithValues, validated_name, inputs, environment):
        template = environment.from_string(
"""CREATE STORAGE INTEGRATION {{ full_name }}
{% if type %}TYPE = {{ type | sql }}
{% endif %}
{%- if storage_provider %}STORAGE_PROVIDER = {{ storage_provider | sql }}
{% endif %}
{%- if storage_aws_role_arn %}STORAGE_AWS_ROLE_ARN = {{ storage_aws_role_arn | sql }}
{% endif %}
{%- if azure_tenant_id %}AZURE_TENANT_ID = {{ azure_tenant_id | sql }}
{% endif %}
{%- if enabled is defined %}ENABLED = {{ enabled | sql }}
{% endif %}
{%- if storage_allowed_locations %}STORAGE_ALLOWED_LOCATIONS = {{ storage_allowed_locations | sql }}
{% endif %}
{%- if storage_blocked_locations %}STORAGE_BLOCKED_LOCATIONS = {{ storage_blocked_locations | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            **inputs
        })

        return sql
