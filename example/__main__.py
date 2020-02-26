import pulumi

from pulumi_snowflake import Provider
from pulumi_snowflake.database import Database
from pulumi_snowflake.fileformat import FileFormat
from pulumi_snowflake.pipe import Pipe
from pulumi_snowflake.schema import Schema
from pulumi_snowflake.stage import Stage
from pulumi_snowflake.storageintegration import StorageIntegration
from pulumi_snowflake.table import Table
from pulumi_snowflake.table.column import Column
from pulumi_snowflake.warehouse import Warehouse, WarehouseSizeValues

"""
# pulumi_snowflake Example Program

The following is a Pulumi program which demonstrates some of pulumi_snowflake's features.  To run the full example,
you will need:

  * Snowflake credentials in your config (see README)
  * a database named "MyDatabase2" and schema named "MySchema2" (or comment out the "Explicit Provider" example below)

"""


"""
## Default provider example

The resources below all use the default provider, which will read the credentials from config.  We can also
specify the database and schema in the config, but in this case they are passed in explicitly.
"""

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

my_table = Table("MyTable",
                 database=my_database.name,
                 schema=my_schema.name,
                 columns=[
                     Column("col_1", "INT", primary_key=True, autoincrement=True),
                     Column("col_2", "VARCHAR", unique=True, collation="utf8"),
                     Column("col_3", "INT", not_null=True, default="123"),
                 ],
                 comment="A test table",
                 data_retention_time_in_days=1
                 )

my_storage_integration = StorageIntegration("MyStorageIntegration",
    enabled=True,
    storage_aws_role_arn='myarn',
    storage_allowed_locations=['s3://allowloc'],
    storage_provider="S3"
)

my_stage = Stage("MyStage",
                 database=my_database.name,
                 schema=my_schema.name,
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
            )


def get_pipe_inputs():
    return pulumi.Output.all(my_stage.full_name, my_table.full_name).apply(lambda args: {
        "stage_name": args[0],
        "table_name": args[1],
    })

my_pipe = Pipe("MyPipe",
               auto_ingest=False,
               comment="A test pipe",
               code=pulumi.Output.all(my_table.full_name, my_stage.full_name).apply(
                   lambda a: f"COPY INTO {a[0]} FROM @{a[1]}"
               ),
               opts=pulumi.ResourceOptions(depends_on=[my_stage,my_table])
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


"""
## Explicit Provider Example

In this example, the File Format resource below is passed an explicit provider.  Any values given to the `Provider`,
such as credentials or database/schema names, override any found in the config.

_NOTE_: MyDatabase2 and MySchema2 must exist for this to work.
"""

my_provider = Provider(database="MyDatabase2", schema="MySchema2")

my_file_format = FileFormat("MyFileFormat",
                            type="CSV",
                            provider=my_provider
                            )

"""
In this example, the File Format resource below is passed an explicit provider, however it is also given an explicit
database and schema.  These values will override those from the provider.
"""

my_file_format_2 = FileFormat("MyFileFormat2",
                              database=my_database.name,
                              schema=my_schema.name,
                              type="JSON",
                              provider=my_provider
                              )

pulumi.export('StorageIntegrationName', my_storage_integration.name)
pulumi.export('FileFormatName', my_file_format.name)
pulumi.export('StageName', my_stage.name)
pulumi.export('DatabaseName', my_database.name)
pulumi.export('SchemaName', my_schema.name)
pulumi.export('WarehouseName', my_warehouse.name)
pulumi.export('PipeName', my_pipe.name)
pulumi.export('TableName', my_table.name)