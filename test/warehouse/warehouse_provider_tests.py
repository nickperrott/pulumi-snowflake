import unittest

from unittest.mock import Mock, call

from pulumi_snowflake.database.database_provider import DatabaseProvider
from pulumi_snowflake.warehouse import WarehouseProvider
from pulumi_snowflake.warehouse.warehouse_scaling_policy_values import WarehouseScalingPolicyValues
from pulumi_snowflake.warehouse.warehouse_size_values import WarehouseSizeValues


class WarehouseProviderTests(unittest.TestCase):

    def test_create_warehouse_simple_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = WarehouseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": 'test_wh',
            "comment": 'test comment',
            "warehouse_size": WarehouseSizeValues.XSMALL,
            "auto_suspend": 300,
            "auto_resume": True,
            "initially_suspended": True,
            "max_cluster_count": 2,
            "min_cluster_count": 3,
            "scaling_policy": WarehouseScalingPolicyValues.STANDARD,
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE WAREHOUSE test_wh",
                f"WAREHOUSE_SIZE = '{WarehouseSizeValues.XSMALL}'",
                f"MAX_CLUSTER_COUNT = 2",
                f"MIN_CLUSTER_COUNT = 3",
                f"SCALING_POLICY = '{WarehouseScalingPolicyValues.STANDARD}'",
                f"AUTO_SUSPEND = 300",
                f"AUTO_RESUME = TRUE",
                f"INITIALLY_SUSPENDED = TRUE",
                f"COMMENT = 'test comment'",
                ""
            ]))
        ])

    def test_create_warehouse_minimal_args(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = WarehouseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            "name": 'test_wh'
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE WAREHOUSE test_wh",
                ""
            ]))
        ])

    def test_delete_warehouse(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = WarehouseProvider(self.get_mock_provider(), mock_connection_provider)
        provider.delete("test_warehouse", {
            "name": "test_warehouse"
        })

        mock_cursor.execute.assert_has_calls([
            call(f"DROP WAREHOUSE test_warehouse")
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
