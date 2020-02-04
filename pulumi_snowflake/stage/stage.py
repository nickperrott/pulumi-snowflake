from typing import Optional

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource

from .stage_file_format import StageFileFormat
from .stage_provider import StageProvider
from .stage_copy_options import StageCopyOptions
from pulumi_snowflake import ConnectionProvider, Credentials


class Stage(Resource):
    """
    Represents a Snowflake Stage.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/create-stage.html
    for more details of parameters.
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
                 file_format: Optional[StageFileFormat] = None,
                 copy_options: Optional[StageCopyOptions] = None,
                 name: Input[Optional[str]] = None,
                 schema: Input[str] = None,
                 comment: Input[Optional[str]] = None,
                 opts: Optional[ResourceOptions] = None):
        """
        :param str resource_name: The logical name of the resource.
        :param StageFileFormat file_format: Specifies the file format for the stage, which can be either.
        :param StageFileFormat copy_options: Specifies one (or more) copy options for the stage.
        :param pulumi.Input[str] comment: Comment string for the integration.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        connection_provider = ConnectionProvider(credentials=Credentials.create_from_config())
        super().__init__(StageProvider(connection_provider), resource_name, {
            'resource_name': resource_name,
            'database': database,
            'copy_options': copy_options.as_dict() if copy_options is not None else None,
            'file_format': file_format.as_dict() if file_format is not None else None,
            'name': name,
            'comment': comment,
            'schema': schema
        }, opts)