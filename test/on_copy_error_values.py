import unittest

from pulumi_snowflake import StageOnCopyErrorValues


class OnCopyErrorValuesTests(unittest.TestCase):

    def test_when_skip_num_with_int_then_constant_is_valid(self):
        self.assertEqual("SKIP_FILE_42", StageOnCopyErrorValues.skip_file(42))

    def test_when_skip_num_with_str_then_constant_is_valid(self):
        self.assertRaises(Exception, StageOnCopyErrorValues.skip_file, '42')

    def test_when_skip_num_percent_with_int_then_constant_is_valid(self):
        self.assertEqual("SKIP_FILE_42%", StageOnCopyErrorValues.skip_file_percent(42))

    def test_when_skip_num_percent_with_str_then_constant_is_valid(self):
        self.assertRaises(Exception, StageOnCopyErrorValues.skip_file_percent, '42')
