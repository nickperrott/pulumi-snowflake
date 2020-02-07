from typing import Optional

from pulumi import Config


class Provider:
    """
    Represents the parameters required to create Snowflake dynamic providers.  By default, parameters which are not
    provided are fetched from config.
    """
    username: str
    password: str
    account_name: str
    role: Optional[str]
    database: Optional[str]
    schema: Optional[str]

    def __init__(
            self,
            username: str = None,
            password: str = None,
            account_name: str = None,
            role: str = None,
            database: str = None,
            schema: str = None
    ):
        config = Config()
        self.username = username if username else config.require('snowflakeUsername')
        self.password = password if password else config.require('snowflakePassword')
        self.account_name = account_name if account_name else config.get('snowflakeAccountName')
        self.role = role if role else config.get('snowflakeRole')
        self.database = database if database else config.get('snowflakeDatabase')
        self.schema = schema if schema else config.get('snowflakeSchema')
