from ..client import Client
from ..provider import Provider
from ..baseprovider.attribute.key_value_attribute import KeyValueAttribute
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class StageProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Stage resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, "STAGE", [
            KeyValueAttribute("url"),
            KeyValueAttribute("storage_integration"),
            KeyValueAttribute("credentials"),
            KeyValueAttribute("encryption"),
            KeyValueAttribute("file_format"),
            KeyValueAttribute("copy_options"),
            KeyValueAttribute("comment")
        ],
        [
            "temporary"
        ])

    def _generate_sql_create_statement(self, validated_name, inputs, environment):
        template = environment.from_string(
"""CREATE{% if temporary %} TEMPORARY{% endif %} STAGE {{ full_name }}
{% if url %}URL = {{ url | sql }}
{% endif %}
{%- if storage_integration %}STORAGE_INTEGRATION = {{ storage_integration | sql }}
{% endif %}
{%- if credentials %}CREDENTIALS = {{ credentials | sql }}
{% endif %}
{%- if encryption %}ENCRYPTION = {{ encryption | sql }}
{% endif %}
{%- if file_format %}FILE_FORMAT = {{ file_format | sql }}
{% endif %}
{%- if copy_options %}COPY_OPTIONS = {{ copy_options | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            **inputs
        })

        return sql
