from typing import Tuple

from jinja2 import Template

from pulumi_snowflake import Client

from ..baseprovider import BaseDynamicProvider
from ..provider import Provider


class DatabaseProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Database resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, "DATABASE", [])

    def _generate_sql_create_statement(self, attributesWithValues, validated_name, inputs):

        # TODO: move these macros to a shared location so they can be used by all resources

        template = Template("""
{%- macro identifier_to_sql(v) -%}
    {{ v }}
{%- endmacro -%}
        
{%- macro str_to_sql(v) -%}
    '{{ v }}'
{%- endmacro -%}

{%- macro num_to_sql(v) -%}
    {%- if v | int == v -%}
        {{ v | int }}
    {%- else -%}
        {{ v }}
    {%- endif -%}
{%- endmacro -%}

{%- macro list_to_sql(l) -%}
    ({% for item in l -%}
        {{ to_sql(item) }}{{ "," if not loop.last }}
    {%- endfor -%})
{%- endmacro -%}

{%- macro dict_to_sql(d) -%}
    ({% for key in d.keys() -%}
        {{ key | upper }} = {{ to_sql(d[key]) }}{{ "," if not loop.last }}
    {%- endfor -%})
{%- endmacro -%}

{%- macro to_sql(v) -%}
    {%- if v is string -%}
        {{ str_to_sql(v) }}
    {%- elif v is integer -%}
        {{ num_to_sql(v) }}
    {%- elif v is float -%}
        {{ num_to_sql(v) }}
    {%- elif v is mapping -%}
        {{ dict_to_sql(v) }}
    {%- elif v is sequence -%}
        {{ list_to_sql(v) }}
    {%- endif -%}
{%- endmacro -%}

CREATE{% if transient %} TRANSIENT{% endif %} DATABASE {{ full_name }}
{% if share %}FROM SHARE {{ identifier_to_sql(share) }}{% endif %}
{% if data_retention_time_in_days %}DATA_RETENTION_TIME_IN_DAYS = {{ to_sql(data_retention_time_in_days) }}{% endif %}
{% if comment %}COMMENT = {{ to_sql(comment) }}{% endif %}
""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            **inputs
        })

        return sql

    def _generate_sql_create_bindings(self, attributesWithValues, inputs):
        return tuple()
