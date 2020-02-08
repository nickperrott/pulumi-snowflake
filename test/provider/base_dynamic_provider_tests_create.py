import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.baseprovider import BaseDynamicProvider


class BaseDynamicProviderTests(unittest.TestCase):

    def test_when_database_and_schema_provided_then_fully_qualified_object_name(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "database": "test_db",
            "schema": "test_schema",
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_db.test_schema.test_name"
            ]))
        ])

    def test_when_database_not_provided_then_short_object_name(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_name"
            ]))
        ])

    def test_when_database_but_no_schema_provided_then_fully_qualified_object_name(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "database": "test_db",
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_db..test_name"
            ]))
        ])

    def test_when_schema_but_no_database_provided_then_short_name(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "schema": "test_schema",
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_name"
            ]))
        ])

    def test_when_database_and_schema_provided_then_appear_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "database": "test_db",
            "schema": "test_schema",
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        self.assertDictEqual(result.outs, {
            "database": "test_db",
            "schema": "test_schema",
            "full_name": "test_db.test_schema.test_name",
            "name": "test_name"
        })

    def test_when_database_not_provided_then_only_full_name_appears_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        self.assertDictEqual(result.outs, {
            "full_name": "test_name",
            "name": "test_name"
        })

    def test_when_database_but_not_schema_provided_then_schema_is_none_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "database": "test_db",
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        self.assertDictEqual(result.outs, {
            "database": "test_db",
            "schema": None,
            "full_name": "test_db..test_name",
            "name": "test_name"
        })

    def test_when_database_and_schema_given_in_provider_then_do_not_appear_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        self.assertDictEqual(result.outs, {
            "full_name": "test_name",
            "name": "test_name"
        })


    def test_when_database_and_schema_given_in_provider_and_overidden_with_none_then_do_not_appear_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": None,
            "schema": None,
        })

        self.assertDictEqual(result.outs, {
            "full_name": "test_name",
            "name": "test_name"
        })


    def test_when_database_but_not_schema_given_in_provider_then_do_not_appear_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = None

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        self.assertDictEqual(result.outs, {
            "full_name": "test_name",
            "name": "test_name"
        })

    def test_when_database_and_schema_given_in_inputs_and_provider_then_inputs_appears_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db",
            "schema": "test_input_schema",
        })

        self.assertDictEqual(result.outs, {
            "database": "test_input_db",
            "schema": "test_input_schema",
            "full_name": "test_input_db.test_input_schema.test_name",
            "name": "test_name"
        })

    def test_when_database_in_inputs_and_provider_and_schema_in_just_provider_then_schema_is_from_provider(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db",
        })

        self.assertDictEqual(result.outs, {
            "database": "test_input_db",
            "schema": "test_provider_schema",
            "full_name": "test_input_db.test_provider_schema.test_name",
            "name": "test_name"
        })

    def test_when_schema_in_inputs_and_provider_and_db_in_just_provider_then_db_output_is_from_provider(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "schema": "test_input_schema",
        })

        self.assertDictEqual(result.outs, {
            "database": "test_provider_db",
            "schema": "test_input_schema",
            "full_name": "test_provider_db.test_input_schema.test_name",
            "name": "test_name"
        })


    def test_when_database_and_schema_given_in_provider_then_they_do_not_appear_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_name"
            ]))
        ])


    def test_when_database_and_schema_given_in_inputs_and_provider_then_inputs_appears_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db",
            "schema": "test_input_schema",
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_input_db.test_input_schema.test_name"
            ]))
        ])


    def test_when_schema_in_inputs_and_provider_and_db_just_in_provider_then_provider_db_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "schema": "test_input_schema",
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_provider_db.test_input_schema.test_name"
            ]))
        ])

    def test_when_database_given_in_inputs_and_provider_and_schema_just_in_provider_then_provider_schema_in_create(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = "test_provider_schema"

        provider = BaseDynamicProvider(mock_provider, mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db",
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE TESTOBJECT test_input_db.test_provider_schema.test_name"
            ]))
        ])

    def test_when_name_has_special_chars_then_identifier_is_enquoted(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])
        provider.create({
            "database": "test~db",
            "schema": "test_schema",
            "name": "test-name",
            "resource_name": "test_resource_name"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f'CREATE TESTOBJECT "test~db".test_schema."test-name"'
            ]))
        ])


    def test_when_name_has_invalid_chars_then_raises_exception(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = BaseDynamicProvider(self.get_mock_provider(), mock_connection_provider, 'TESTOBJECT', [])

        self.assertRaises(Exception, provider.create, {
            "database": "test~db",
            "schema": "test_schema",
            "name": 'test"name',
            "resource_name": "test_resource_name"
        })

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
