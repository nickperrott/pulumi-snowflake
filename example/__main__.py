import pulumi

from pulumi_snowflake.stage import StageOnCopyErrorValues, StageMatchByColumnNameValues
from pulumi_snowflake import CompressionValues, NoneToken, AutoToken
from pulumi_snowflake.fileformat import FileFormat, FileFormatType
from pulumi_snowflake.stage import Stage, StageFileFormat, StageCopyOptions
from pulumi_snowflake.storageintegration import AWSStorageIntegration
from pulumi_snowflake.utf8_token import UTF8Token


# Enter your snowflake DB name and (optionally) Schema here
snowflake_db_name = "FIRSTTEST"
snowflake_schema_name = "FIRSTSCHEMA"

my_storage_integration = AWSStorageIntegration("MyStorageIntegration",
                                               enabled=True,
                                               storage_aws_role_arn='myarn',
                                               storage_allowed_locations=['s3://allowloc']
                                               )

pulumi.export('StorageIntegrationName', my_storage_integration.name)
pulumi.export('StorageIntegrationType', my_storage_integration.type)
pulumi.export('StorageIntegrationArn', my_storage_integration.storage_aws_role_arn)

my_file_format = FileFormat("MyFileFormat",
                            name=None,
                            database=snowflake_db_name,
                            schema=snowflake_schema_name,
                            type=FileFormatType.CSV
                            )

pulumi.export('FileFormatType', my_file_format.type)
pulumi.export('FileFormatName', my_file_format.name)
pulumi.export('FileFormatDatabase', my_file_format.database)
pulumi.export('FileFormatSchema', my_file_format.schema)

my_stage = Stage("MyStage",
                 name=my_storage_integration.name.apply(lambda n: f"MyStage_{n}"),
                 file_format=StageFileFormat(
                     type="CSV",
                     null_if=["NULL","n"],
                     compression=CompressionValues.GZIP,
                     record_delimiter=';',
                     field_delimiter=NoneToken(),
                     encoding=UTF8Token(),
                     date_format=AutoToken(),
                     skip_header=1
                 ),
                 database=snowflake_db_name,
                 schema=snowflake_schema_name,
                 copy_options=StageCopyOptions(
                         size_limit=100,
                         on_error=StageOnCopyErrorValues.skip_file_percent(20),
                         match_by_column_name=StageMatchByColumnNameValues.CASE_INSENSITIVE,
                     ),
                 )

pulumi.export('StageName', my_stage.name)
