from pulumi_snowflake import ConnectionProvider

from ..baseprovider import BaseDynamicProvider, KeyValueAttribute
from ..provider import Provider
from ..validation import Validation


class SchemaProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake Schema resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: ConnectionProvider):
        super().__init__(provider_params, connection_provider, "SCHEMA", [
            KeyValueAttribute("data_retention_time_in_days"),
            KeyValueAttribute("comment")
        ], [
            "transient"
        ])

    def _get_full_object_name(self, inputs, name):
        """
        Schemas are unique since they are the only object scoped to databases.  Their fully-qualified is therefore
        different.
        """
        name = Validation.enquote_identifier(name)

        if inputs.get("database"):
            database = inputs["database"]
            database = Validation.enquote_identifier(database)
            return f"{database}.{name}"
        else:
            return name
