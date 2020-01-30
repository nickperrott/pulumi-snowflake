import pulumi
from pulumi_snowflake.fileformat import FileFormat, FileFormatType
from pulumi_snowflake.storageintegration import AWSStorageIntegration

# Enter your snowflake DB name and (optionally) Schema here
snowflake_db_name = "FIRSTTEST"
snowflake_schema_name = "FIRSTSCHEMA"

myRes = FileFormat("MyFileFormat",
     name=None,
     database=snowflake_db_name,
     schema=snowflake_schema_name,
     type=FileFormatType.CSV
 )

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
pulumi.export('FileFormatDatabase', myRes.database)
pulumi.export('FileFormatSchema', myRes.schema)

myStorageIntegration = AWSStorageIntegration("MyStorageIntegration",
    name='MyStorageIntegrationName',
    enabled=False,
    storage_aws_role_arn='myarn',
    storage_allowed_locations=['s3://allowloc']
)

pulumi.export('StorageIntegrationName', myStorageIntegration.name)
pulumi.export('StorageIntegrationType', myStorageIntegration.type)
pulumi.export('StorageIntegrationArn', myStorageIntegration.storage_aws_role_arn)