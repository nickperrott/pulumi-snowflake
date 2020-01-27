import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.file_format_provider import FileFormatProvider


class FileFormatProviderTests(unittest.TestCase):

    # Put outputs on fileformat object

    def test_when_call_delete_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"USE DATABASE database_name"),
            call(f"DROP FILE FORMAT test_file_format")
        ])

    def test_when_call_delete_with_schema_none_then_use_schema_is_not_executed(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name",
            "schema": None
        })

        mock_cursor.execute.assert_has_calls([
            call(f"USE DATABASE database_name"),
            call(f"DROP FILE FORMAT test_file_format")
        ])

    def test_when_call_delete_with_schema_then_use_schema_is_executed(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name",
            "schema": "schema_name"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"USE DATABASE database_name"),
            call(f"USE SCHEMA schema_name"),
            call(f"DROP FILE FORMAT test_file_format")
        ])

    def test_when_call_delete_and_id_invalid_then_error_thrown(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(mock_connection_provider)

        self.assertRaises(Exception, provider.delete, "invalid-id", {
            "database": "database_name"
        })

    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mock_connection
        return mock_connection_provider
