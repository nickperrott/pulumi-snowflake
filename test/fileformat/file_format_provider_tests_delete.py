import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.fileformat import FileFormatProvider


class FileFormatProviderTests(unittest.TestCase):

    def test_when_call_delete_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP FILE FORMAT database_name..test_file_format")
        ])

    def test_when_call_delete_with_schema_none_then_schema_is_not_used(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name",
            "schema": None
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP FILE FORMAT database_name..test_file_format")
        ])

    def test_when_call_delete_with_schema_then_uses_schema(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_file_format", {
            "database": "database_name",
            "schema": "schema_name"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP FILE FORMAT database_name.schema_name.test_file_format")
        ])

    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mock_connection
        return mock_connection_provider

    def get_mock_provider(self):
        mock_provider = Mock()
        mock_provider.database = None
        mock_provider.schema = None
        return mock_provider
