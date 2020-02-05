import unittest

from pulumi_snowflake import NoneToken
from pulumi_snowflake.stage import ExternalStageEncryption


class ExternalStageEncryptionTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        encryption = ExternalStageEncryption(
            type=NoneToken(),
            master_key="test-none",
            kms_key_id="test-none"
        )
        self.assertDictEqual(encryption.as_dict(), {
            "type": NoneToken(),
            "master_key": "test-none",
            "kms_key_id": "test-none"
        })