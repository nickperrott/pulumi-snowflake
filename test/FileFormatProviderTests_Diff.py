import unittest
from unittest.mock import Mock

from pulumi_snowflake.FileFormatProvider import FileFormatProvider
from pulumi_snowflake.FileFormatType import FileFormatType


class FileFormatProviderTests(unittest.TestCase):

    # Put outputs on fileformat object

    def testWhenTypeAndDatabaseAreUnchangedThenNoChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name"
        }, {
            "type": FileFormatType.CSV,
            "database": "database_name"
        })

        self.assertFalse(result.changes)
        self.assertSetEqual(set(result.replaces), set())

    def testWhenTypeChangedThenNeedsChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name"
        }, {
            "type": FileFormatType.JSON,
            "database": "database_name"
        })

        self.assertTrue(result.changes)
        self.assertSetEqual(set(result.replaces), {"type"})

    def testWhenDatabaseChangedThenNeedsChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name"
        }, {
            "type": FileFormatType.CSV,
            "database": "database_name_changed"
        })

        self.assertTrue(result.changes)
        self.assertSetEqual(set(result.replaces), {"database"})

    def testWhenNameChangedThenNeedsChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name",
            "name": "name_old"
        }, {
            "type": FileFormatType.CSV,
            "database": "database_name",
            "name": "name_new"
        })

        self.assertTrue(result.changes)
        self.assertSetEqual(set(result.replaces), {"name"})

    def testWhenNameNotGivenInNewsThenNoChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name",
            "name": "name_old"
        }, {
            "type": FileFormatType.CSV,
            "database": "database_name"
        })

        self.assertFalse(result.changes)
        self.assertSetEqual(set(result.replaces), set())

    def testWhenSchemaChangedThenNeedsChange(self):
        provider = FileFormatProvider(Mock())
        result = provider.diff("test_file_format", {
            "type": FileFormatType.CSV,
            "database": "database_name",
            "schema": "schema_old"
        }, {
            "type": FileFormatType.CSV,
            "database": "database_name",
            "schema": "schema_new"
        })

        self.assertTrue(result.changes)
        self.assertSetEqual(set(result.replaces), {"schema"})
