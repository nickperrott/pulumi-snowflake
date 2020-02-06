import pulumi

from pulumi_snowflake.fileformat import FileFormat
from pulumi_snowflake.stage import Stage
from pulumi_snowflake.storageintegration import AWSStorageIntegration


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
                            type="CSV"
                            )

pulumi.export('FileFormatType', my_file_format.type)
pulumi.export('FileFormatName', my_file_format.name)
pulumi.export('FileFormatDatabase', my_file_format.database)
pulumi.export('FileFormatSchema', my_file_format.schema)

my_stage = Stage("MyStage",
                 name=my_storage_integration.name.apply(lambda n: f"MyStage_{n}"),
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
                 database=snowflake_db_name,
                 schema=snowflake_schema_name,
                 copy_options={
                     "size_limit":100,
                     "on_error": "skip_file_45%",
                     "match_by_column_name": "case_insensitive",
                }
            )

# Boolean: check python type
# Identifier: special function if necessary
# integer: detect from type
# string: detect from type
# string list (or list in general): detect from type
# struct: detect if it's a dict
# auto, none etc can be strings?

pulumi.export('StageName', my_stage.name)
