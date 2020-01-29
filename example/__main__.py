import pulumi
from pulumi_snowflake.fileformat import FileFormat, FileFormatType

# Enter your snowflake DB name and (optionally) Schema here
snowflake_db_name = "FIRSTTEST"
snowflake_schema_name = "FIRSTSCHEMA"

myRes = FileFormat("MyFileFormat",
     name=None,
     database=snowflake_db_name,
     schema=snowflake_schema_name,
     type=FileFormatType.JSON
 )

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
pulumi.export('FileFormatDatabase', myRes.database)
pulumi.export('FileFormatSchema', myRes.schema)
