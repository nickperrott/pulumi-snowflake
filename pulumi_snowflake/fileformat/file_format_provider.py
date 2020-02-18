from ..client import Client
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider
from pulumi_snowflake.validation import Validation


class FileFormatProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake FileFormat resources.
    """

    connection_provider: Client

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, "FILE FORMAT", [
            KeyValueAttribute("type"),
            KeyValueAttribute("comment")
        ])


    def _generate_sql_create_statement(self, attributesWithValues, validated_name, inputs, environment):
        template = environment.from_string(
"""CREATE FILE FORMAT {{ full_name }}
{% if type %}TYPE = {{ type | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            **inputs
        })

        return sql

    def _generate_sql_create_bindings(self, attributesWithValues, inputs):
        return tuple()
