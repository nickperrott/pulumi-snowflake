from .. import Client
from ..baseprovider import BaseDynamicProvider
from ..provider import Provider
from ..validation import Validation


class GrantProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake database grants.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="Grant")

    def generate_sql_create_statement(self, name, inputs, environment):
        template = environment.from_string(
            """GRANT {% for priv in privileges %} {{priv}}{% if not loop.last %},{% endif %}{% endfor %}
ON DATABASE {{database}} TO ROLE {{role}}
{%- if grant_option %} WITH GRANT OPTION
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
            """REVOKE
{% for priv in privileges %} {{priv}} {% if not loop.last %},{% endif %}
{% endfor %}
            ON DATABASE {{database}} FROM ROLE {{role}} CASCADE
""")
        sql = template.render({
            **inputs,
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })
        return sql

    def _get_full_object_name(self, inputs, name):
        return name
