from typing import List, Optional

from pulumi import Input, Output, ResourceOptions

from pulumi_snowflake import ConnectionProvider, Credentials
from .storage_integration import StorageIntegration
from .aws_storage_integration_provider import AWSStorageIntegrationProvider


class AWSStorageIntegration(StorageIntegration):

    DEFAULT_STORAGE_PROVIDER = 'S3'
    """
    A constant representing the default storage provider.
    """

    storage_provider: Output[str]
    """
    Specifies the cloud storage provider that stores your data files.  At time of writing only S3 is available.
    """

    storage_aws_role_arn: Output[str]
    """
    The ARN of IAM role that grants privileges on the S3 bucket containing data files.
    """

    def __init__(self,
                 resource_name: str,
                 enabled: Input[bool],
                 storage_aws_role_arn: Input[str],
                 storage_allowed_locations: Input[List[str]],
                 name: str = None,
                 type: Input[str] = StorageIntegration.DEFAULT_STORAGE_INTEGRATION_TYPE,
                 storage_provider: Input[str] = DEFAULT_STORAGE_PROVIDER,
                 storage_blocked_locations: Input[Optional[List[str]]] = None,
                 comment: Input[Optional[str]] = None,
                 opts: Optional[ResourceOptions] = None):
        """
        :param str resource_name: The logical name of the resource.
        :param pulumi.Input[bool] enabled: Whether or not the storage integration is available for use.
        :param pulumi.Input[str] storage_aws_role_arn: The ARN of IAM role that grants privileges on the S3 bucket
                                 containing data files.
        :param pulumi.Input[List[str]] storage_allowed_locations: Explicitly limits external stages that use the
                                 integration to reference one or more storage locations.
        :param pulumi.Input[Optional[List[str]]] storage_blocked_locations: Explicitly prohibits external stages that
                                 use the integration from referencing one or more storage locations.
        :param pulumi.Input[str] type: The storage integration type.
        :param pulumi.Input[str] storage_provider: The cloud storage provider.
        :param pulumi.Input[str] comment: Comment string for the integration.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        connection_provider = ConnectionProvider(credentials=Credentials.create_from_config())
        super().__init__(AWSStorageIntegrationProvider(connection_provider), resource_name, {
            'resource_name': resource_name,
            'name': name,
            'enabled': enabled,
            'storage_aws_role_arn': storage_aws_role_arn,
            'storage_allowed_locations': storage_allowed_locations,
            'storage_blocked_locations': storage_blocked_locations,
            'type': type,
            'storage_provider': storage_provider,
            'comment': comment
        }, opts)