import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.schema import SchemaProvider


class SchemaProviderTests(unittest.TestCase):

    def test_create_schema_simple_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_schema",
            "comment": "test_comment",
            "transient": False,
            "data_retention_time_in_days": 7
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE SCHEMA test_schema",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'",
                ""
            ]))
        ])

    def test_create_schema_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_schema",
            "comment": None,
            "transient": False,
            "data_retention_time_in_days": None
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE SCHEMA test_schema",
                ""
            ]))
        ])

    def test_when_create_schema_with_transient_true_then_appears_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_schema",
            "comment": "test_comment",
            "transient": True,
            "data_retention_time_in_days": 7
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TRANSIENT SCHEMA test_schema",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'",
                ""
            ]))
        ])


    def test_when_create_schema_with_database_true_then_appears_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test_schema",
            "comment": "test_comment",
            "transient": True,
            "data_retention_time_in_days": 7,
            "database": "test_db"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TRANSIENT SCHEMA test_db.test_schema",
                f"DATA_RETENTION_TIME_IN_DAYS = 7",
                f"COMMENT = 'test_comment'",
                ""
            ]))
        ])

    def test_delete_schema(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_schema", {
            "name": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP SCHEMA test_schema")
        ])


    def test_when_name_has_special_chars_then_identifier_is_enquoted(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = SchemaProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": "test~schema",
            "database": "test-database"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f'CREATE SCHEMA "test-database"."test~schema"',
                ""
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
