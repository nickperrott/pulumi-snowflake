from pulumi import Config


class Credentials:
    """
    Represents Snowflake credentials
    """
    username: str
    password: str
    account_name: str
    role: str

    def __init__(
            self,
            username: str,
            password: str,
            account_name: str,
            role: str
    ):
        self.username = username
        self.password = password
        self.account_name = account_name
        self.role = role

    @staticmethod
    def create_from_config():
        config = Config()
        return Credentials(
            username=config.require('snowflakeUsername'),
            password=config.require('snowflakePassword'),
            account_name=config.require('snowflakeAccountName'),
            role=config.get('snowflakeRole')
        )
