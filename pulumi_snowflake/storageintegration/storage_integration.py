from typing import Optional, List

from pulumi import Output, ResourceOptions
from pulumi.dynamic import Resource, ResourceProvider

class StorageIntegration(Resource):
    """
    Represents a Snowflake Storage Integration.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/create-storage-integration.html
    for more details of parameters.
    """

    DEFAULT_STORAGE_INTEGRATION_TYPE = 'EXTERNAL_STAGE'
    """
    A constant representing the default type value.
    """

    name: Output[str]
    """
    The name of the storage integration in Snowflake.
    """

    type: Output[str]
    """
    The storage integration type.  At time of writing, Snowflake only allows "EXTERNAL_STAGE".
    """

    enabled: Output[bool]
    """
    Whether or not the storage integration is available for use.
    """

    storage_allowed_locations: Output[List[str]]
    """
    Explicitly limits external stages that use the integration to reference one or more storage locations.
    """

    storage_blocked_locations: Output[Optional[List[str]]]
    """
    Explicitly prohibits external stages that use the integration from referencing one or more storage locations.
    """

    comment: Output[Optional[str]]
    """
    Comment string for the integration.
    """

    def __init__(self,
                 provider: ResourceProvider,
                 name: str,
                 props: 'Inputs',
                 opts: Optional[ResourceOptions] = None) -> None:
        super().__init__(provider, name, props, opts)


