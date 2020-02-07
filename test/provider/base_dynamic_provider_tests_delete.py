import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.baseprovider import BaseDynamicProvider


class BaseDynamicProviderTests(unittest.TestCase):

    def test_when_database_and_schema_provided_then_fully_qualified_object_name_in_delete(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.delete("test_name", {
            "database": "test_db",
            "schema": "test_schema",
            "name": "test_name",
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"DROP TESTOBJECT test_db.test_schema.test_name"
            ]))
        ])


    def test_when_database_not_provided_then_short_object_name_in_delete(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.delete("test_name", {
            "name": "test_name",
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"DROP TESTOBJECT test_name"
            ]))
        ])

    def test_when_database_and_schema_given_in_provider_then_do_not_appear_in_delete(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        provider.delete("test_name", {
            "name": "test_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"DROP TESTOBJECT test_name"
            ]))
        ])


    # HELPERS

    def get_mock_provider(self):
        mock_provider = Mock()
        mock_provider.database = None
        mock_provider.schema = None
        return mock_provider

    def get_mock_connection_provider(self, mock_cursor):
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mock_connection
        return mock_connection_provider
