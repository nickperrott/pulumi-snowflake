import pulumi
import pulumi_snowflake as snowflake
from pulumi_snowflake.FileFormatType import FileFormatType

myRes = snowflake.FileFormat("MyTestFileFormat", "FirstTest", FileFormatType.CSV,
                             "NewTestFileFormat")

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
