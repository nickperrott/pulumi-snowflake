import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.baseprovider import BaseDynamicProvider

class TestProvider(BaseDynamicProvider):

    def __init__(self, provider_params, connection_provider):
        super().__init__(provider_params, connection_provider, "Test")

    def generate_sql_create_statement(self, validated_name, inputs, environment):
        template = environment.from_string(
            """CREATE TESTOBJECT {{ full_name }}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, validated_name)
        })

        return sql

class BaseDynamicProviderTests(unittest.TestCase):

    def test_when_database_and_schema_provided_then_fully_qualified_object_name(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(self.get_mock_provider(), mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
        result = provider.create({
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": None,
            "schema": None,
        })

        self.assertDictEqual(result.outs, {
            "full_name": "test_name",
            "name": "test_name",
            "database": None,
            "schema": None,
        })


    def test_when_database_but_not_schema_given_in_provider_then_do_not_appear_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        mock_provider = self.get_mock_provider()
        mock_provider.database = "test_provider_db"
        mock_provider.schema = None

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

        provider = TestProvider(mock_provider, mock_connection_provider)
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

    def test_when_invalid_identifier_then_raises_exception(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        class TestIdProvider(BaseDynamicProvider):
            def __init__(self, provider_params, connection_provider):
                super().__init__(provider_params, connection_provider, "TestId")

            def generate_sql_create_statement(self, validated_name, inputs, environment):
                template = environment.from_string("{{ test_id | sql_identifier }}")
                sql = template.render(**inputs)
                return sql

        provider = TestIdProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            "test_id": "My-Id",
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db",
        })

    def test_when_invalid_string_then_raises_exception(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        class TestIdProvider(BaseDynamicProvider):
            def __init__(self, provider_params, connection_provider):
                super().__init__(provider_params, connection_provider, "TestId")

            def generate_sql_create_statement(self, validated_name, inputs, environment):
                template = environment.from_string("{{ test_str | sql }}")
                sql = template.render(**inputs)
                return sql

        provider = TestIdProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            "test_str": "my_test_string'; DROP TABLE USERS --",
            "name": "test_name",
            "resource_name": "test_resource_name",
            "database": "test_input_db"
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