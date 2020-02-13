from typing import Tuple

from jinja2 import Template

from pulumi_snowflake import Client

from ..baseprovider import BaseDynamicProvider, KeyValueAttribute, BaseAttribute
from ..baseprovider.sql_converter import SqlConverter
from ..provider import Provider
from ..validation import Validation


class DatabaseProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Database resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, "DATABASE", [])

    def _generate_sql_create_statement(self, attributesWithValues, validated_name, inputs):
        template = Template(
"""CREATE{% if is_transient %} TRANSIENT{% endif %} DATABASE {{ full_name }}
{% if share %}FROM SHARE {{ share }}{% endif %}
{% if data_retention_time_in_days %}DATA_RETENTION_TIME_IN_DAYS = {{ data_retention_time_in_days }}{% endif %}
{% if comment %}COMMENT = {{ comment }}{% endif %}
"""
        )

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name),
            "is_transient": inputs.get("transient"),
            "share": SqlConverter.to_identifier(inputs.get("share")),
            "data_retention_time_in_days": SqlConverter.to_sql(inputs.get("data_retention_time_in_days")),
            "comment": SqlConverter.to_sql(inputs.get("comment"))
        })

        return sql

    def _generate_sql_create_bindings(self, attributesWithValues, inputs):
        return tuple()
