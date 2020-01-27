import pulumi
import pulumi_snowflake as snowflake

# Enter your snowflake DB name and (optionally) Schema here
snowflake_db_name = "FIRSTTEST"
snowflake_schema_name = "FIRSTSCHEMA"

myRes = snowflake.FileFormat("MyFileFormat",
     name=None,
     database=snowflake_db_name,
     schema=snowflake_schema_name,
     type=snowflake.FileFormatType.JSON
 )

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
pulumi.export('FileFormatDatabase', myRes.database)
pulumi.export('FileFormatSchema', myRes.schema)
