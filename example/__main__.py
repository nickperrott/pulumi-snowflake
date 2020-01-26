import sys
import pulumi
import pulumi_snowflake as snowflake

myRes = snowflake.FileFormat("MyTestFileFormat", 'CSV')

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
