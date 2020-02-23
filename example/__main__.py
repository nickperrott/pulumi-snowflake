import pulumi

from pulumi_snowflake import Provider
from pulumi_snowflake.database import Database
from pulumi_snowflake.fileformat import FileFormat
from pulumi_snowflake.pipe import Pipe
from pulumi_snowflake.schema import Schema
from pulumi_snowflake.stage import Stage
from pulumi_snowflake.storageintegration import StorageIntegration
from pulumi_snowflake.warehouse import Warehouse, WarehouseScalingPolicyValues, WarehouseSizeValues

# Enter your snowflake DB name and (optionally) Schema here
my_provider = Provider(database="FIRSTTEST", schema="FIRSTSCHEMA")

my_storage_integration = StorageIntegration("MyStorageIntegration",
    enabled=True,
    storage_aws_role_arn='myarn',
    storage_allowed_locations=['s3://allowloc'],
    storage_provider="S3",
    provider=my_provider
)


# The resource below does not provide a database and schema, so it uses the provider values

my_stage = Stage("MyStage",
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
                     "size_limit": 100,
                     "on_error": "skip_file_45%"
                },
                provider=my_provider
            )


# The resource below provides an explicit database and schema which overrides the provider values

my_file_format = FileFormat("MyFileFormat",
    database="SECONDDATABASE",
    schema="SECONDSCHEMA",
    name=None,
    type="CSV",
    provider=my_provider
)


my_database = Database("MyDatabase",
                       comment="A test database",
                       transient=False,
                       data_retention_time_in_days=1
                       )


my_schema = Schema("MySchema",
                   database=my_database.name,
                   comment="A test schema",
                   transient=True,
                   data_retention_time_in_days=1
                   )

my_warehouse = Warehouse("MyWarehouse",
                         comment="A test warehouse",
                         warehouse_size=WarehouseSizeValues.XSMALL,
                         auto_suspend=300,
                         min_cluster_count=1,
                         max_cluster_count=1,
                         auto_resume=True,
                         initially_suspended=True
                         )

# Pipe example - this required a table named FIRSTTABLE to exist.

my_pipe = Pipe("MyPipe",
               auto_ingest=False,
               comment="A test pipe",
               code=my_stage.name.apply(lambda n: f"copy into FIRSTTABLE from @{n}")
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

pulumi.export('SchemaName', my_schema.name)

pulumi.export('WarehouseName', my_warehouse.name)

#pulumi.export('PipeName', my_pipe.name)