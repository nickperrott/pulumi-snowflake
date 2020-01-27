import pulumi
import pulumi_snowflake as snowflake
from pulumi_snowflake.file_format_type import FileFormatType

# Enter your snowflake DB name and (optionally) Schema here
snowflakeDbName = "FIRSTTEST"
snowflakeSchemaName = "FIRSTSCHEMA"

myRes = snowflake.FileFormat("MyFileFormat",
    name=None,
    database=snowflakeDbName,
    schema=snowflakeSchemaName,
    type=FileFormatType.JSON
)

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
pulumi.export('FileFormatDatabase', myRes.database)
pulumi.export('FileFormatSchema', myRes.schema)
