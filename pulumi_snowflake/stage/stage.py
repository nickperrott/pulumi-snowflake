from typing import Optional

from pulumi import Input, ResourceOptions, Output
from pulumi.dynamic import Resource

from .stage_provider import StageProvider
from pulumi_snowflake import ConnectionProvider, Credentials


class StageFileFormat:
    format_name: Input[Optional[str]]
    type: Input[Optional[str]]
    #TODO format type options

    def __init__(self,
                 format_name: Input[Optional[str]] = None,
                 type: Input[Optional[str]] = None):
        self.format_name = format_name
        self.type = type


class Stage(Resource):
    file_format: Optional[StageFileFormat]
    comment: Output[Optional[str]]

    #TODO comments below

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
        :param StageFileFormat file_format:
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