import pulumi

from pulumi_snowflake import Provider
from pulumi_snowflake.database import Database
from pulumi_snowflake.fileformat import FileFormat
from pulumi_snowflake.stage import Stage
from pulumi_snowflake.storageintegration import StorageIntegration


# Enter your snowflake DB name and (optionally) Schema here
my_provider = Provider(database="FIRSTTEST", schema="FIRSTSCHEMA")

my_storage_integration = StorageIntegration("MyStorageIntegration",
    enabled=True,
    storage_aws_role_arn='myarn',
    storage_allowed_locations=['s3://allowloc'],
    provider=my_provider
)


# The resource below does not provide a database and schema, so it uses the provider values

my_file_format = FileFormat("MyFileFormat",
    name=None,
    type="CSV",
    provider=my_provider
)

# The resource below provides an explicit database and schema which overrides the provider values

my_stage = Stage("MyStage",
                 name=my_storage_integration.name.apply(lambda n: f"MyStage_{n}"),
                 database="SECONDDATABASE",
                 schema="SECONDSCHEMA",
                 file_format={
                     "type": "CSV",
                     "null_if": ["NULL","n"],
                     "compression": "gzip",
                     "record_delimiter": ';',
                     "field_delimiter": "NONE",
                     "encoding": "UTF8",
                     "date_format": "AUTO",
                     "skip_header": 1
                 },
                 copy_options={
                     "size_limit":100,
                     "on_error": "skip_file_45%",
                     "match_by_column_name": "case_insensitive",
                },
                provider=my_provider
            )


my_database = Database("MyDatabase",
                       comment="A test database",
                       transient=False,
                       data_retention_time_in_days=1
                       )

pulumi.export('StorageIntegrationName', my_storage_integration.name)
pulumi.export('StorageIntegrationType', my_storage_integration.type)
pulumi.export('StorageIntegrationArn', my_storage_integration.storage_aws_role_arn)

pulumi.export('FileFormatType', my_file_format.type)
pulumi.export('FileFormatName', my_file_format.name)
pulumi.export('FileFormatDatabase', my_file_format.database)
pulumi.export('FileFormatSchema', my_file_format.schema)

pulumi.export('StageName', my_stage.name)

pulumi.export('DatabaseName', my_database.name)
pulumi.export('DatabaseTransient', my_database.transient)
pulumi.export('DatabaseShare', my_database.share)
