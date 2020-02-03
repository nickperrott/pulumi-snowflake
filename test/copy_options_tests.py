import unittest

from pulumi_snowflake import OnCopyErrorValues, MatchByColumnNameValues
from pulumi_snowflake.copy_options import CopyOptions


class CopyOptionsTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        copy_options = CopyOptions(
            size_limit=42,
            on_error=OnCopyErrorValues.CONTINUE,
            purge=True,
            return_failed_only=False,
            match_by_column_name=MatchByColumnNameValues.CASE_SENSITIVE,
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
            "match_by_column_name": MatchByColumnNameValues.CASE_SENSITIVE,
            "enforce_length": True,
            "truncate_columns": False,
            "force": True,
            "load_uncertain_files": False
        })