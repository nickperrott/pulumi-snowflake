import unittest

from pulumi_snowflake.stage import ExternalStageCredentials


class ExternalStageCredentialsTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        creds = ExternalStageCredentials(
            aws_key_id="test-key-id",
            aws_secret_key="test-aws-secret-key",
            aws_token="test-aws-token",
            aws_role="test-aws-role",
            azure_sas_token="test-azure-sas-token",
        )
        self.assertDictEqual(creds.as_dict(), {
            "aws_key_id": "test-key-id",
            "aws_secret_key": "test-aws-secret-key",
            "aws_token": "test-aws-token",
            "aws_role": "test-aws-role",
            "azure_sas_token": "test-azure-sas-token",
        })
