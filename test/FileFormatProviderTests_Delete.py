import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.FileFormatProvider import FileFormatProvider


class FileFormatProviderTests(unittest.TestCase):

    # Make DB name an output of create
    # Allow choice of schema
    # Put outputs on fileformat object

    def testWhenCallDeleteThenSqlIsGenerated(self):
        mockCursor = Mock()
        mockConnectionProvider = self.getMockConnectionProvider(mockCursor)

        provider = FileFormatProvider(mockConnectionProvider)
        provider.delete("test_file_format", {
            "database": "database_name"
        })

        mockCursor.execute.assert_has_calls([
            call(f"USE DATABASE database_name"),
            call(f"DROP FILE FORMAT test_file_format")
        ])

    def testWhenCallDeleteAndIdInvalidThenErrorThrown(self):
        mockCursor = Mock()
        mockConnectionProvider = self.getMockConnectionProvider(mockCursor)

        provider = FileFormatProvider(mockConnectionProvider)

        self.assertRaises(Exception, provider.delete, "invalid-id", {
            "database": "database_name"
        })

    # HELPERS

    def getMockConnectionProvider(self, mockCursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mockCursor
        mockConnectionProvider = Mock()
        mockConnectionProvider.get.return_value = mockConnection
        return mockConnectionProvider
