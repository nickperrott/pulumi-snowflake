import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.storageintegration import StorageIntegration, StorageIntegrationProvider


class StorageIntegrationProviderTests(unittest.TestCase):

    def test_when_call_create_with_required_fields_and_name_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create(self.get_standard_inputs())

        (allowed1, allowed2) = self.get_standard_inputs()['storage_allowed_locations']

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STORAGE INTEGRATION {self.get_standard_inputs()['name']}",
                f"TYPE = '{self.get_standard_inputs()['type']}'",
                f"STORAGE_PROVIDER = '{self.get_standard_inputs()['storage_provider']}'",
                f"STORAGE_AWS_ROLE_ARN = '{self.get_standard_inputs()['storage_aws_role_arn']}'",
                "ENABLED = TRUE",
                f"STORAGE_ALLOWED_LOCATIONS = ('{allowed1}','{allowed2}')",
                ""
            ]))
        ])

    def test_when_call_create_with_required_fields_and_name_then_outputs_are_returned(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create({
            **self.get_standard_inputs()
        })

        self.assertDictEqual(result.outs, {
            **self.get_standard_outputs(),
            "full_name": "test_name"
        })

    def test_when_call_create_with_enabled_false_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            **self.get_standard_inputs(),
            'enabled': False
        })

        (allowed1,allowed2) = self.get_standard_inputs()['storage_allowed_locations']

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STORAGE INTEGRATION {self.get_standard_inputs()['name']}",
                f"TYPE = '{self.get_standard_inputs()['type']}'",
                f"STORAGE_PROVIDER = '{self.get_standard_inputs()['storage_provider']}'",
                f"STORAGE_AWS_ROLE_ARN = '{self.get_standard_inputs()['storage_aws_role_arn']}'",
                "ENABLED = FALSE",
                f"STORAGE_ALLOWED_LOCATIONS = ('{allowed1}','{allowed2}')",
                ""
            ]))
        ])


    def test_when_call_create_with_one_allowed_location_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            **self.get_standard_inputs(),
            'storage_allowed_locations': [ 'allowed_loc' ]
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STORAGE INTEGRATION {self.get_standard_inputs()['name']}",
                f"TYPE = '{self.get_standard_inputs()['type']}'",
                f"STORAGE_PROVIDER = '{self.get_standard_inputs()['storage_provider']}'",
                f"STORAGE_AWS_ROLE_ARN = '{self.get_standard_inputs()['storage_aws_role_arn']}'",
                "ENABLED = TRUE",
                f"STORAGE_ALLOWED_LOCATIONS = ('allowed_loc')",
                ""
            ]))
        ])

    def test_when_call_create_with_name_then_storage_integration_name_is_returned_as_id(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create(self.get_standard_inputs())

        self.assertEqual(result.id, self.get_standard_inputs()["name"])

    def test_when_optional_fields_given_then_appear_in_outputs(self):
        fieldValues = {
            'storage_blocked_locations': ['blocked_loc_1'],
            'storage_blocked_locations': [ 'blocked_loc_1', 'blocked_loc_2' ],
            'comment': 'a test comment'
        }

        for field in fieldValues.keys():
            mock_connection_provider = self.get_mock_connection_provider(Mock())
            provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)

            result = provider.create({
                **self.get_standard_inputs(),
                field: fieldValues[field]
            })

            self.assertDictEqual(result.outs, {
                **self.get_standard_outputs(),
                "full_name": "test_name",
                field: fieldValues[field]
            })

    def test_when_optional_fields_with_bindings_given_then_appear_in_sql(self):
        fieldValues = {
            'storage_blocked_locations': ['blocked_loc_1'],
            'storage_blocked_locations': [ 'blocked_loc_1', 'blocked_loc_2' ],
            'comment': 'a test comment',
            'azure_tenant_id': 'test_tenant'
        }

        fieldSql = {
            'storage_blocked_locations': "STORAGE_BLOCKED_LOCATIONS = ('blocked_loc_1')",
            'storage_blocked_locations': "STORAGE_BLOCKED_LOCATIONS = ('blocked_loc_1','blocked_loc_2')",
            'comment': "COMMENT = 'a test comment'",
            'azure_tenant_id': "AZURE_TENANT_ID = 'test_tenant'"
        }

        for field in fieldValues.keys():
            mock_cursor = Mock()
            mock_connection_provider = self.get_mock_connection_provider(mock_cursor)
            provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)

            inputs = {
                **self.get_standard_inputs(),
                field: fieldValues[field]
            }

            provider.create(inputs)

            (allowed1, allowed2) = self.get_standard_inputs()['storage_allowed_locations']

            mock_cursor.execute.assert_has_calls([
                call("\n".join([
                    f"CREATE STORAGE INTEGRATION {self.get_standard_inputs()['name']}",
                    f"TYPE = '{self.get_standard_inputs()['type']}'",
                    f"STORAGE_PROVIDER = '{self.get_standard_inputs()['storage_provider']}'",
                    f"STORAGE_AWS_ROLE_ARN = '{self.get_standard_inputs()['storage_aws_role_arn']}'",
                    "ENABLED = TRUE",
                    f"STORAGE_ALLOWED_LOCATIONS = ('{allowed1}','{allowed2}')",
                    fieldSql[field],
                    ""
                ]))
            ])

    def test_when_call_create_without_name_then_name_is_autogenerated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        resourceName = 'test_resource_name'
        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create({
            **self.get_standard_inputs(),
            'resource_name': resourceName,
            'name': None,
        })

        self.assertRegex(result.outs["name"], resourceName + '_[a-f,0-9]{7}')
        self.assertEqual(result.id, result.outs["name"])

    def test_when_invalid_resource_name_given_and_name_is_autogenerated_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())

        resourceName = 'test_resource_name'
        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'name': None,
            'resource_name': 'invalid-name'
        })


    def test_when_neither_resource_name_nor_name_given_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())
        provider = StorageIntegrationProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'name': None,
            'resource_name': None
        })

    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mockConnection
        return mock_connection_provider

    def get_standard_inputs(self):
        return {
            'name': 'test_name',
            'type': StorageIntegration.DEFAULT_STORAGE_INTEGRATION_TYPE,
            'enabled': True,
            'storage_provider': 'S3',
            'storage_aws_role_arn': 'test_role_arn',
            'storage_allowed_locations': [ 'allowed_loc_1', 'allowed_loc_2' ],
            'comment': None,
            'storage_blocked_locations': None,
        }

    def get_standard_outputs(self):
        return {
            **self.get_standard_inputs()
        }

    # HELPERS

    def get_mock_provider(self):
        mock_provider = Mock()
        mock_provider.database = None
        mock_provider.schema = None
        return mock_provider
