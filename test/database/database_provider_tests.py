import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.database.database_provider import DatabaseProvider


class DatabaseProviderTests(unittest.TestCase):

    def test_create_database_simple_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = DatabaseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_db",
            "comment": "test_comment",
            "transient": False,
            "data_retention_time_in_days": 7,
            "share": None
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE DATABASE test_db",
                f"",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'"
            ]))
        ])

    def test_create_database_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = DatabaseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_db",
            "comment": None,
            "transient": None,
            "data_retention_time_in_days": None,
            "share": None
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([f"CREATE DATABASE test_db", "", "", ""]))
            ])

    def test_when_create_database_with_transient_true_then_appears_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = DatabaseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_db",
            "comment": "test_comment",
            "transient": True,
            "data_retention_time_in_days": 7,
            "share": None
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TRANSIENT DATABASE test_db",
                "",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'"
            ]))
        ])

    def test_when_create_database_with_share_then_appears_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = DatabaseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_db",
            "comment": "test_comment",
            "transient": False,
            "data_retention_time_in_days": 7,
            "share": "test.share"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE DATABASE test_db",
                f"FROM SHARE test.share",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'"
            ]))
        ])

    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mockConnection
        return mock_connection_provider

    def get_mock_provider(self):
        mock_provider = Mock()
        mock_provider.database = None
        mock_provider.schema = None
        return mock_provider
