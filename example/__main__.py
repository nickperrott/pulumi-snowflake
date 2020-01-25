import sys
import pulumi_snowflake as snowflake

myRes = snowflake.FileFormat("MyTestFileFormat", {})