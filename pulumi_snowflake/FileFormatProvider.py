import pulumi
from pulumi.dynamic import ResourceProvider, CreateResult
import snowflake.connector


class FileFormatProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake FileFormat resources
    """

    def create(self, inputs):

        ctx = snowflake.connector.connect(
            user=inputs["snowflakeUsername"],
            password=inputs["snowflakePassword"],
            account=inputs["snowflakeAccountName"]
        )

        cs = ctx.cursor()

        version = "novalue"

        try:
            cs.execute("SELECT current_version()")
            one_row = cs.fetchone()
            version = f"{one_row[0]}"
            print(version)
        finally:
            cs.close()
        ctx.close()

        return CreateResult(id_="foo", outs={
            "name": version
        })
