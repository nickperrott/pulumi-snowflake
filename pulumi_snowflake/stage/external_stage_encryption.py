from typing import Union, Optional

from pulumi import Input

from pulumi_snowflake import NoneToken


class ExternalStageEncryption:

    def __init__(self,
                 type: Input[Optional[Union[str, NoneToken]]] = None,
                 master_key: Input[Optional[str]] = None,
                 kms_key_id: Input[Optional[str]] = None,
                 ):
        self.type = type
        self.master_key = master_key
        self.kms_key_id = kms_key_id

    def as_dict(self):
        fields = [
            "type",
            "master_key",
            "kms_key_id",
        ]
        return { field: getattr(self, field) for field in fields }
