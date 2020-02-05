import unittest

from pulumi_snowflake.stage import StageCopyOptions, StageOnCopyErrorValues, StageMatchByColumnNameValues


class StageCopyOptionsTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        copy_options = StageCopyOptions(
            size_limit=42,
            on_error=StageOnCopyErrorValues.CONTINUE,
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