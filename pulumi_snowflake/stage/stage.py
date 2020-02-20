from typing import Optional

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource
from .stage_provider import StageProvider
from ..provider import Provider
from ..client import Client


class Stage(Resource):
    """
    Represents a Snowflake Stage.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/create-stage.html
    for more details of parameters.
    """

    url: Output[Optional[str]]
    """
    Specifies the URL for the external location used to store data files for loading/unloading.
    """

    storage_integration: Output[Optional[str]]
    """
    Specifies the name of the storage integration used to delegate authentication responsibility for external cloud
    storage to a Snowflake identity and access management (IAM) entity.
    """

    credentials: Output[Optional[dict]]
    """
    Specifies the security credentials for connecting to AWS and accessing the private/protected S3 bucket where the
    files to load/unload are staged.
    """

    encryption: Output[Optional[dict]]
    """
    Specifies the encryption settings used to encrypt files unloaded to external storage.
    """

    file_format: Output[Optional[dict]]
    """
    Specifies the file format for the stage, which can be either.
    """

    copy_options: Output[Optional[dict]]
    """
    Specifies one (or more) copy options for the stage.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the stage.
    """

    def __init__(self,
                 resource_name: str,
                 database: Input[str] = None,
                 schema: Input[str] = None,
                 url: Input[Optional[str]] = None,
                 storage_integration: Input[Optional[str]] = None,
                 credentials: Optional[dict] = None,
                 encryption: Optional[dict] = None,
                 file_format: Optional[dict] = None,
                 copy_options: Optional[dict] = None,
                 name: Input[Optional[str]] = None,
                 comment: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):
        """
        :param str resource_name: The logical name of the resource.
        :param pulumi.Input[str] database:
        :param pulumi.Input[Optional[str]] url:
        :param pulumi.Input[Optional[str]] storage_integration: Specifies the name of the storage integration used to
            delegate authentication responsibility for external cloud storage to a Snowflake identity and access
            management (IAM) entity
        :param Optional[ExternalStageCredentials] credentials: Specifies the security credentials for connecting
            to AWS and accessing the private/protected S3 bucket where the files to load/unload are staged.
        :param Optional[ExternalStageEncryption] encryption: Specifies the encryption settings used to encrypt
            files unloaded to external storage.
        :param StageFileFormat Optional[file_format]: Specifies the file format for the stage, which can be either.
        :param StageFileFormat Optional[copy_options]: Specifies one (or more) copy options for the stage.
        :param pulumi.Input[str] comment: Comment string for the integration.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(StageProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'database': database,
            'url': url,
            'storage_integration': storage_integration,
            'credentials': credentials,
            'encryption': encryption,
            'copy_options': copy_options,
            'file_format': file_format,
            'name': name,
            'comment': comment,
            'schema': schema
        }, opts)
