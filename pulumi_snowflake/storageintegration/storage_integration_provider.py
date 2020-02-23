from ..client import Client
from ..provider import Provider
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class StorageIntegrationProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Storage Integration resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="Storage Integration")

    def generate_sql_create_statement(self, validated_name, inputs, environment):
        template = environment.from_string(
"""CREATE {{ resource_type | upper }} {{ full_name }}
{% if type %}TYPE = {{ type | sql }}
{% endif %}
{%- if storage_provider %}STORAGE_PROVIDER = {{ storage_provider | sql }}
{% endif %}
{%- if storage_aws_role_arn %}STORAGE_AWS_ROLE_ARN = {{ storage_aws_role_arn | sql }}
{% endif %}
{%- if enabled is boolean %}ENABLED = {{ enabled | sql }}
{% endif %}
{%- if storage_allowed_locations %}STORAGE_ALLOWED_LOCATIONS = {{ storage_allowed_locations | sql }}
{% endif %}
{%- if storage_blocked_locations %}STORAGE_BLOCKED_LOCATIONS = {{ storage_blocked_locations | sql }}
{% endif %}
{%- if azure_tenant_id %}AZURE_TENANT_ID = {{ azure_tenant_id | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            "resource_type": self.resource_type,
            **inputs
        })

        return sql

    def generate_sql_drop_statement(self, validated_name, inputs, environment):
        template = environment.from_string("DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            "resource_type": self.resource_type
        })
        return sql
