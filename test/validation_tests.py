import unittest

from pulumi_snowflake.validation import Validation


class ValidationTests(unittest.TestCase):

    def test_when_identifier_none_then_enquote_identifier_returns_none(self):
        self.assertEqual(Validation.enquote_identifier(None), None)

    def test_when_valid_identifier_then_enquote_identifier_returns_original(self):
        id = "TEST_identifier$123"
        self.assertEqual(Validation.enquote_identifier(id), id)

    def test_when_invalid_identifier_then_is_valid_identifier_returns_false(self):
        ids = [
            "test-",
            "test#",
            "test ",
            "0test"
        ]

        for id in ids:
            self.assertEqual(Validation.enquote_identifier(id), f'"{id}"')

    def test_when_identifier_is_not_enquotable_then_raises_exception(self):
        self.assertRaises(Exception, Validation.enquote_identifier, 'test"id')

    def test_when_is_enquoted_identifier_valid_called_with_valid_identifier_then_true(self):
        self.assertEqual(Validation.is_enquoted_identifier_valid("test_id"), True)

    def test_when_is_enquoted_identifier_valid_called_with_valid_enquoted_identifier_then_true(self):
        self.assertEqual(Validation.is_enquoted_identifier_valid("test-id"), True)

    def test_when_is_enquoted_identifier_valid_called_with_invalid_enquoted_identifier_then_false(self):
        self.assertEqual(Validation.is_enquoted_identifier_valid('test"id'), False)
