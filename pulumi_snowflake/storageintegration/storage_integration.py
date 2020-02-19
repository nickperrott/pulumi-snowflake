from typing import Optional, List

from pulumi import Output, ResourceOptions, Input
from pulumi.dynamic import Resource

from ..provider import Provider
from ..client import Client
from .storage_integration_provider import StorageIntegrationProvider


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

    storage_provider: Output[str]
    """
    Specifies the cloud storage provider that stores your data files.  At time of writing only S3 is available.
    """

    storage_aws_role_arn: Output[str]
    """
    The ARN of IAM role that grants privileges on the S3 bucket containing data files.
    """

    azure_tenant_id: Output[str]
    """
    Specifies the ID for your Office 365 tenant that the allowed and blocked storage accounts belong to.
    """

    def __init__(self,
                 resource_name: str,
                 enabled: Input[bool],
                 storage_allowed_locations: Input[List[str]],
                 storage_aws_role_arn: Input[Optional[str]] = None,
                 azure_tenant_id: Input[Optional[str]] = None,
                 name: str = None,
                 type: Input[str] = DEFAULT_STORAGE_INTEGRATION_TYPE,
                 storage_provider: Input[Optional[str]] = None,
                 storage_blocked_locations: Input[Optional[List[str]]] = None,
                 comment: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):
        """
        :param str resource_name: The logical name of the resource.
        :param pulumi.Input[bool] enabled: Whether or not the storage integration is available for use.
        :param pulumi.Input[str] storage_aws_role_arn: The ARN of IAM role that grants privileges on the S3 bucket
                                 containing data files.
        :param pulumi.Input[str] storage_aws_role_arn: Specifies the ID for your Office 365 tenant that the allowed and
                                 blocked storage accounts belong to.
        :param pulumi.Input[List[str]] storage_allowed_locations: Explicitly limits external stages that use the
                                 integration to reference one or more storage locations.
        :param pulumi.Input[Optional[List[str]]] storage_blocked_locations: Explicitly prohibits external stages that
                                 use the integration from referencing one or more storage locations.
        :param pulumi.Input[str] type: The storage integration type.
        :param pulumi.Input[str] storage_provider: The cloud storage provider.
        :param pulumi.Input[str] comment: Comment string for the integration.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        provider = provider if provider else Provider()
        connection_provider = Client(provider=provider)

        super().__init__(StorageIntegrationProvider(provider, connection_provider), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'enabled': enabled,
            'storage_aws_role_arn': storage_aws_role_arn,
            'azure_tenant_id': azure_tenant_id,
            'storage_allowed_locations': storage_allowed_locations,
            'storage_blocked_locations': storage_blocked_locations,
            'type': type,
            'storage_provider': storage_provider,
            'comment': comment
        }, opts)
