from typing import Optional

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource

from .external_stage_credentials import ExternalStageCredentials
from .external_stage_encryption import ExternalStageEncryption
from .stage_file_format import StageFileFormat
from .stage_provider import StageProvider
from .stage_copy_options import StageCopyOptions
from ..connection_provider import ConnectionProvider
from ..credentials import Credentials


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

    credentials: Output[Optional[ExternalStageCredentials]]
    """
    Specifies the security credentials for connecting to AWS and accessing the private/protected S3 bucket where the
    files to load/unload are staged.
    """

    encryption: Output[Optional[ExternalStageEncryption]]
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
                 database: Input[str],
                 url: Input[Optional[str]] = None,
                 storage_integration: Input[Optional[str]] = None,
                 credentials: Optional[ExternalStageCredentials] = None,
                 encryption: Optional[ExternalStageEncryption] = None,
                 file_format: Optional[StageFileFormat] = None,
                 copy_options: Optional[StageCopyOptions] = None,
                 name: Input[Optional[str]] = None,
                 schema: Input[str] = None,
                 comment: Input[Optional[str]] = None,
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
        connection_provider = ConnectionProvider(credentials=Credentials.create_from_config())
        super().__init__(StageProvider(connection_provider), resource_name, self.serialize_inputs_to_dict({
            'resource_name': resource_name,
            'database': database,
            'url': url,
            'storage_integration': storage_integration,
            'credentials': credentials.as_dict() if credentials else None,
            'encryption': encryption.as_dict() if encryption else None,
            'copy_options': copy_options.as_dict() if copy_options is not None else None,
            'file_format': file_format.as_dict() if file_format is not None else None,
            'name': name,
            'comment': comment,
            'schema': schema
        }), opts)

    def serialize_inputs_to_dict(self, parent_dict):
        """
        Pulumi serializes inputs before passing them to the provider, however this package aims to present a
        strongly-typed object-oriented interface.  This method recursively finds values which can be represented as
        dictionaries (such as objects with an `as_dict` method) and serializes them.
        """

        def value_to_dict_value(value):

            if hasattr(value, "as_dict") and callable(value.as_dict):
                value = value.as_dict()

            if isinstance(value, dict):
                return self.serialize_inputs_to_dict(value)

            return value

        return {
            k: value_to_dict_value(parent_dict[k]) for k in parent_dict
        }

