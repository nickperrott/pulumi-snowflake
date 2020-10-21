from .. import Client
from ..baseprovider import BaseDynamicProvider
from ..provider import Provider
from ..validation import Validation


class RoleProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Role resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="Role")

    def generate_sql_create_statement(self, name, inputs, environment):
        template = environment.from_string(
            """CREATE {{ resource_type | upper }} {{ full_name }}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}
""")

        sql = template.render({
            **inputs,
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type,
        })

        return sql

    def generate_sql_drop_statement(self, name, inputs, environment):
        template = environment.from_string(
            "DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })
        return sql

    def _get_full_object_name(self, inputs, name):
        return name
