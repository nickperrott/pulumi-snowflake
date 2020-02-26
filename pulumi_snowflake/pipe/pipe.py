from typing import Optional

from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import Resource

from .. import Client
from ..provider import Provider
from .pipe_provider import PipeProvider


class Pipe(Resource):
    """
    Represents a Snowflake Pipe.  See https://docs.snowflake.net/manuals/sql-reference/sql/create-pipe.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the pipe in Snowflake.
    """

    auto_ingest: Output[Optional[bool]]
    """
    Specifies whether to automatically load data files from the specified external stage and optional path when event
    notifications are received from a configured message service.
    """

    aws_sns_topic: Output[Optional[str]]
    """
    Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket.
    """

    integration: Output[Optional[str]]
    """
    Specifies the existing notification integration used to access an Azure storage queue.
    """

    comment: Output[Optional[str]]
    """
    Specifies a comment for the pipe.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 name: Input[Optional[str]] = None,
                 auto_ingest: Input[Optional[bool]] = None,
                 aws_sns_topic: Input[Optional[str]] = None,
                 integration: Input[Optional[str]] = None,
                 code: Input[Optional[str]] = None,
                 comment: Input[Optional[str]] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None
                 ):

        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(PipeProvider(provider, client), resource_name, {
            'resource_name': resource_name,
            'full_name': None,
            'name': name,
            'auto_ingest': auto_ingest,
            'aws_sns_topic': aws_sns_topic,
            'integration': integration,
            'code': code,
            'comment': comment
        }, opts)
