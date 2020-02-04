import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.stage import StageProvider


class StageTests(unittest.TestCase):

    def test_create_stage(self):

        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StageProvider(mock_connection_provider)
        provider.create({
            "file_format": {
                'format_name': 'test_file_format',
                'type': None
            },
            "comment": "test_comment",
            "name": "test_stage",
            "database": "test_database",
            "schema": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STAGE test_database.test_schema.test_stage",
                f"FILE_FORMAT = (FORMAT_NAME = %s)",
                f"COMMENT = %s"
            ]), ('test_file_format', 'test_comment'))
        ])


    def test_when_file_format_not_given_then_input_is_none(self):

        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StageProvider(mock_connection_provider)
        provider.create({
            "file_format": None,
            "comment": "test_comment",
            "name": "test_stage",
            "database": "test_database",
            "schema": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STAGE test_database.test_schema.test_stage",
                f"COMMENT = %s"
            ]), ('test_comment',))
        ])


    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mockConnection
        return mock_connection_provider
