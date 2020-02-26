import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.table import TableProvider
from pulumi_snowflake.table.column import Column


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
            "columns": [
                Column("test_col", "INT").as_dict()
            ]
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                "CREATE TABLE test_db.test_schema.test_table",
                "(",
                "  test_col INT",
                ")",
                "CLUSTER BY ( to_date(timestamp),id )",
                "DATA_RETENTION_TIME_IN_DAYS = 7",
                "COMMENT = 'test_comment'",
                ""
            ]))
        ])


    def test_create_table_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_table",
            "columns": [
                Column("test_col", "INT").as_dict()
            ]
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                "CREATE TABLE test_table",
                "(",
                "  test_col INT",
                ")",
                ""
            ]))
        ])

    def test_create_table_with_column_attributes(self):

        attr_values = [
            { "name": "collation",     "value": "utf8", "sql": "test_col INT COLLATE 'utf8'" },
            { "name": "default",       "value": "123",  "sql": "test_col INT DEFAULT 123" },
            { "name": "autoincrement", "value": True,   "sql": "test_col INT AUTOINCREMENT" },
            { "name": "autoincrement", "value": False,  "sql": "test_col INT" },
            { "name": "not_null",      "value": True,   "sql": "test_col INT NOT NULL" },
            { "name": "not_null",      "value": False,  "sql": "test_col INT" },
            { "name": "unique",        "value": True,   "sql": "test_col INT UNIQUE" },
            { "name": "unique",        "value": False,  "sql": "test_col INT" },
            { "name": "primary_key",   "value": True,   "sql": "test_col INT PRIMARY KEY" },
            { "name": "primary_key",   "value": False,  "sql": "test_col INT" }
        ]

        for attribute in attr_values:
            mock_cursor = Mock()
            mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

            provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
            provider.create({
                "name": "test_table",
                "database": None,
                "schema": None,
                "comment": None,
                "cluster_by": None,
                "data_retention_time_in_days": None,
                "columns": [
                    {
                        "name": "test_col",
                        "type": "INT",
                        attribute["name"]: attribute["value"]
                    }
                ]
            })

            mock_cursor.execute.assert_has_calls([
                call("\n".join([
                    "CREATE TABLE test_table",
                    "(",
                    f"  {attribute['sql']}",
                    ")",
                    ""
                ]))
            ])


    def test_create_table_multiple_cols(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TableProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_table",
            "columns": [
                Column("test_col1", "INT").as_dict(),
                Column("test_col2", "INT").as_dict(),
                Column("test_col3", "INT").as_dict()
            ]
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                "CREATE TABLE test_table",
                "(",
                "  test_col1 INT,",
                "  test_col2 INT,",
                "  test_col3 INT",
                ")",
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
