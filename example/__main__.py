import pulumi
import pulumi_snowflake as snowflake
from pulumi_snowflake.FileFormatType import FileFormatType

myRes = snowflake.FileFormat("MyTestFileFormat",
    database="FirstTest",
    type=FileFormatType.CSV
)

pulumi.export('FileFormatType', myRes.type)
pulumi.export('FileFormatName', myRes.name)
