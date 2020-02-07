from typing import Tuple

from pulumi_snowflake import ConnectionProvider

from ..baseprovider import BaseDynamicProvider, KeyValueAttribute, BaseAttribute
from ..provider import Provider
from ..validation import Validation


class DatabaseProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Database resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "DATABASE", [
            FromShareAttribute("share"),
            KeyValueAttribute("data_retention_time_in_days"),
            KeyValueAttribute("comment")
        ], [
            "transient"
        ])


class FromShareAttribute(BaseAttribute):

    def generate_sql(self, value) -> str:
        if value is not None:
            Validation.validate_qualified_object_name(value)
            return f'FROM SHARE {value}'
        else:
            return ''

    def generate_bindings(self, value) -> Tuple:
        return tuple()


