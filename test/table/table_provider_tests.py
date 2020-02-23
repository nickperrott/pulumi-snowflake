import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.table import TableProvider


class TableProviderTests(unittest.TestCase):


    def test_create_table_simple_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_table",
            "database": "test_db",
            "schema": "test_schema",
            "comment": "test_comment",
            "cluster_by": ['to_date(timestamp)', 'id'],
            "data_retention_time_in_days": 7,
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TABLE test_db.test_schema.test_table",
                f"CLUSTER BY ( to_date(timestamp),id )",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'",
                ""
            ]))
        ])


    def test_create_table_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_table"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TABLE test_table",
                ""
            ]))
        ])

    def test_delete_table(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_table", {
            "name": "test_table"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP TABLE test_table")
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
