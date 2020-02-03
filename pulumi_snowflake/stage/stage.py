from typing import Optional

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource

from .stage_file_format import StageFileFormat
from .stage_provider import StageProvider
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
                 file_format: Optional[StageFileFormat],
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
            'file_format': {
                'format_name': file_format.format_name,
                'type': file_format.type
            },
            'name': name,
            'comment': comment,
            'schema': schema
        }, opts)