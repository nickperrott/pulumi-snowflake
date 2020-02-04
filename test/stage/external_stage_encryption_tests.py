import unittest

from pulumi_snowflake import NoneValue
from pulumi_snowflake.stage.external_stage_encryption import ExternalStageEncryption


class ExternalStageEncryptionTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        encryption = ExternalStageEncryption(
            type=NoneValue(),
            master_key="test-none",
            kms_key_id="test-none"
        )
        self.assertDictEqual(encryption.as_dict(), {
            "type": NoneValue(),
            "master_key": "test-none",
            "kms_key_id": "test-none"
        })