from typing import Tuple

from pulumi_snowflake import ConnectionProvider

from ..baseprovider import BaseDynamicProvider, KeyValueAttribute, BaseAttribute
from ..provider import Provider


class PipeProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Pipe resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "PIPE", [
            KeyValueAttribute('auto_ingest'),
            KeyValueAttribute('aws_sns_topic'),
            KeyValueAttribute('integration'),
            KeyValueAttribute('comment'),
            VerbatimAttribute('code')
        ])


class VerbatimAttribute(BaseAttribute):

    def generate_sql(self, value) -> str:
        return f"AS {value}"

    def generate_bindings(self, value) -> Tuple:
        return tuple()
