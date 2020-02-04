from typing import Optional

from pulumi import Input


class ExternalStageCredentials:

    def __init__(self,
                 aws_key_id: Input[Optional[str]] = None,
                 aws_secret_key: Input[Optional[str]] = None,
                 aws_token: Input[Optional[str]] = None,
                 aws_role: Input[Optional[str]] = None,
                 azure_sas_token: Input[Optional[str]] = None,
                 ):
        self.aws_key_id = aws_key_id
        self.aws_secret_key = aws_secret_key
        self.aws_token = aws_token
        self.aws_role = aws_role
        self.azure_sas_token = azure_sas_token

    def as_dict(self):
        fields = [
            "aws_key_id",
            "aws_secret_key",
            "aws_token",
            "aws_role",
            "azure_sas_token",
        ]
        return { field: getattr(self, field) for field in fields }
