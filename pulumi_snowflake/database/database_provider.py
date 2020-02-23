from pulumi_snowflake import Client

from ..baseprovider import BaseDynamicProvider
from ..provider import Provider


class DatabaseProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Database resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="Database")

    def generate_sql_create_statement(self, name, inputs, environment):
        template = environment.from_string(
"""CREATE{% if transient %} TRANSIENT{% endif %} {{ resource_type | upper }} {{ full_name }}
{% if share %}FROM SHARE {{ share | sql_identifier }}
{% endif %}
{%- if data_retention_time_in_days %}DATA_RETENTION_TIME_IN_DAYS = {{ data_retention_time_in_days | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}
""")

        sql = template.render({
            **inputs,
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })

        return sql

    def generate_sql_drop_statement(self, name, inputs, environment):
        template = environment.from_string("DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })
        return sql
