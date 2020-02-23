from .. import Client
from ..baseprovider import BaseDynamicProvider
from ..provider import Provider
from ..validation import Validation


class SchemaProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Schema resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="Schema")

    def generate_sql_create_statement(self, name, inputs, environment):
        template = environment.from_string(
"""CREATE{% if transient %} TRANSIENT{% endif %} {{ resource_type | upper }} {{ full_name }}
{% if data_retention_time_in_days %}DATA_RETENTION_TIME_IN_DAYS = {{ data_retention_time_in_days | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}
""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type,
            **inputs
        })

        return sql

    def generate_sql_drop_statement(self, name, inputs, environment):
        template = environment.from_string("DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })
        return sql

    def _get_full_object_name(self, inputs, name):
        """
        Schemas are unique since they are the only object scoped to databases.  Their fully-qualified
        name format is therefore different.
        """
        name = Validation.enquote_identifier(name)

        if inputs.get("database"):
            database = inputs["database"]
            database = Validation.enquote_identifier(database)
            return f"{database}.{name}"
        else:
            return name
