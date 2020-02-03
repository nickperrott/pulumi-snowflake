import unittest

from pulumi_snowflake import OnCopyErrorValues, StageMatchByColumnNameValues
from pulumi_snowflake.stage.stage_copy_options import StageCopyOptions


class CopyOptionsTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        copy_options = StageCopyOptions(
            size_limit=42,
            on_error=OnCopyErrorValues.CONTINUE,
            purge=True,
            return_failed_only=False,
            match_by_column_name=StageMatchByColumnNameValues.CASE_SENSITIVE,
            enforce_length=True,
            truncate_columns=False,
            force=True,
            load_uncertain_files=False
        )
        self.assertDictEqual(copy_options.as_dict(), {
            "size_limit": 42,
            "on_error": "CONTINUE",
            "purge": True,
            "return_failed_only": False,
            "match_by_column_name": StageMatchByColumnNameValues.CASE_SENSITIVE,
            "enforce_length": True,
            "truncate_columns": False,
            "force": True,
            "load_uncertain_files": False
        })