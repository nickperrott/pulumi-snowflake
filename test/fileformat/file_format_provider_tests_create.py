import unittest
from unittest.mock import Mock, call

from pulumi_snowflake.fileformat import FileFormatProvider


class FileFormatProviderTests(unittest.TestCase):

    def test_when_call_create_with_name_and_type_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create(self.get_standard_inputs())

        fullName = f"{self.get_standard_inputs()['database']}..{self.get_standard_inputs()['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                f"TYPE = 'CSV'",
                ""
            ]))
        ])


    def test_when_call_create_with_options_then_sql_is_generated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            **self.get_standard_inputs(),
            "compression": "GZIP",
            "record_delimiter": "g",
            "field_delimiter": "h",
            "file_extension": "gfd",
            "skip_header": 123,
            "skip_blank_lines": True,
            "date_format": "dd",
            "time_format": "mm",
            "timestamp_format": "ts",
            "binary_format": "HEX",
            "escape": "esc",
            "escape_unenclosed_field": "esuf",
            "trim_space": False,
            "field_optionally_enclosed_by": "f",
            "null_if": ["nf","nu"],
            "error_on_column_count_mismatch": True,
            "replace_invalid_characters": False,
            "validate_utf8": True,
            "empty_field_as_null": False,
            "skip_byte_order_mark": True,
            "encoding": "UTF8",
            "enable_octal": True,
            "allow_duplicate": False,
            "strip_outer_array": True,
            "strip_null_values": False,
            "ignore_utf8_errors": True,
            "skip_byte_order_mark": False,
            "binary_as_text": True,
            "snappy_compression": False,
            "preserve_space": True,
            "strip_outer_element": False,
            "disable_snowflake_data": True,
            "disable_auto_convert": False,
        })

        fullName = f"{self.get_standard_inputs()['database']}..{self.get_standard_inputs()['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                f"TYPE = 'CSV'",
                f"COMPRESSION = 'GZIP'",
                f"RECORD_DELIMITER = 'g'",
                f"FIELD_DELIMITER = 'h'",
                f"FILE_EXTENSION = 'gfd'",
                f"SKIP_HEADER = 123",
                f"SKIP_BLANK_LINES = TRUE",
                f"DATE_FORMAT = 'dd'",
                f"TIME_FORMAT = 'mm'",
                f"TIMESTAMP_FORMAT = 'ts'",
                f"BINARY_FORMAT = 'HEX'",
                f"ESCAPE = 'esc'",
                f"ESCAPE_UNENCLOSED_FIELD = 'esuf'",
                f"TRIM_SPACE = FALSE",
                f"FIELD_OPTIONALLY_ENCLOSED_BY = 'f'",
                f"NULL_IF = ('nf','nu')",
                f"ERROR_ON_COLUMN_COUNT_MISMATCH = TRUE",
                f"REPLACE_INVALID_CHARACTERS = FALSE",
                f"VALIDATE_UTF8 = TRUE",
                f"EMPTY_FIELD_AS_NULL = FALSE",
                f"SKIP_BYTE_ORDER_MARK = FALSE",
                f"ENCODING = 'UTF8'",
                f"ENABLE_OCTAL = TRUE",
                f"ALLOW_DUPLICATE = FALSE",
                f"STRIP_OUTER_ARRAY = TRUE",
                f"STRIP_NULL_VALUES = FALSE",
                f"IGNORE_UTF8_ERRORS = TRUE",
                f"BINARY_AS_TEXT = TRUE",
                f"SNAPPY_COMPRESSION = FALSE",
                f"PRESERVE_SPACE = TRUE",
                f"STRIP_OUTER_ELEMENT = FALSE",
                f"DISABLE_SNOWFLAKE_DATA = TRUE",
                f"DISABLE_AUTO_CONVERT = FALSE",
                ""
            ]))
        ])

    def test_when_call_create_with_bools_false_then_still_appear_in_sql(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            'database': 'test_database_name',
            'type': None,
            'resource_name': 'pulumi_test_file_format',
            'name': 'test_file_format',
            'comment': None,
            "skip_blank_lines": False,
            "trim_space": False,
            "error_on_column_count_mismatch": False,
            "replace_invalid_characters": False,
            "validate_utf8": False,
            "empty_field_as_null": False,
            "skip_byte_order_mark": False,
            "enable_octal": False,
            "allow_duplicate": False,
            "strip_outer_array": False,
            "strip_null_values": False,
            "ignore_utf8_errors": False,
            "binary_as_text": False,
            "snappy_compression": False,
            "preserve_space": False,
            "strip_outer_element": False,
            "disable_snowflake_data": False,
            "disable_auto_convert": False,
        })

        fullName = f"{self.get_standard_inputs()['database']}..{self.get_standard_inputs()['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                f"SKIP_BLANK_LINES = FALSE",
                f"TRIM_SPACE = FALSE",
                f"ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE",
                f"REPLACE_INVALID_CHARACTERS = FALSE",
                f"VALIDATE_UTF8 = FALSE",
                f"EMPTY_FIELD_AS_NULL = FALSE",
                f"SKIP_BYTE_ORDER_MARK = FALSE",
                f"ENABLE_OCTAL = FALSE",
                f"ALLOW_DUPLICATE = FALSE",
                f"STRIP_OUTER_ARRAY = FALSE",
                f"STRIP_NULL_VALUES = FALSE",
                f"IGNORE_UTF8_ERRORS = FALSE",
                f"BINARY_AS_TEXT = FALSE",
                f"SNAPPY_COMPRESSION = FALSE",
                f"PRESERVE_SPACE = FALSE",
                f"STRIP_OUTER_ELEMENT = FALSE",
                f"DISABLE_SNOWFLAKE_DATA = FALSE",
                f"DISABLE_AUTO_CONVERT = FALSE",
                ""
            ]))
        ])


    def test_when_call_create_with_bools_none_then_do_not_appear_in_sql(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            'database': 'test_database_name',
            'type': None,
            'resource_name': 'pulumi_test_file_format',
            'name': 'test_file_format',
            'comment': None,
            "skip_blank_lines": None,
            "trim_space": None,
            "error_on_column_count_mismatch": None,
            "replace_invalid_characters": None,
            "validate_utf8": None,
            "empty_field_as_null": None,
            "skip_byte_order_mark": None,
            "enable_octal": None,
            "allow_duplicate": None,
            "strip_outer_array": None,
            "strip_null_values": None,
            "ignore_utf8_errors": None,
            "binary_as_text": None,
            "snappy_compression": None,
            "preserve_space": None,
            "strip_outer_element": None,
            "disable_snowflake_data": None,
            "disable_auto_convert": None,
        })

        fullName = f"{self.get_standard_inputs()['database']}..{self.get_standard_inputs()['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                ""
            ]))
        ])


    def test_when_call_create_with_schema_then_executes_in_schema(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        provider.create({
            **self.get_standard_inputs(),
            "schema": "test_schema"
        })

        fullName = f"{self.get_standard_inputs()['database']}.test_schema.{self.get_standard_inputs()['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                f"TYPE = 'CSV'",
                ""
            ]))
        ])

    def test_when_call_create_with_name_and_type_then_outputs_are_returned(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create(self.get_standard_inputs())

        fullName = f"{self.get_standard_inputs()['database']}..{self.get_standard_inputs()['name']}"

        self.assertDictEqual(result.outs, {
            "comment": None,
            "name": self.get_standard_inputs()["name"],
            "full_name": fullName,
            "type": self.get_standard_inputs()["type"],
            "database": self.get_standard_inputs()["database"],
            "schema": None
        })
    
    def test_when_call_create_with_schema_then_appears_in_outputs(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create({
            **self.get_standard_inputs(),
            "schema": "test_schema",
        })

        fullName = f"{self.get_standard_inputs()['database']}.test_schema.{self.get_standard_inputs()['name']}"

        self.assertDictEqual(result.outs, {
            "name": self.get_standard_inputs()["name"],
            "full_name": fullName,
            "type": self.get_standard_inputs()["type"],
            "database": self.get_standard_inputs()["database"],
            "schema": "test_schema",
            "comment": None
        })


    def test_when_call_create_with_name_and_type_then_file_format_name_is_returned_as_id(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create(self.get_standard_inputs())

        self.assertEqual(result.id, self.get_standard_inputs()["name"])

    def test_when_call_create_without_name_then_name_is_autogenerated(self):
        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)
        result = provider.create({
            **self.get_standard_inputs(),
            'name': None,
        })

        fullName = f"{self.get_standard_inputs()['database']}..{result.outs['name']}"

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE FILE FORMAT {fullName}",
                f"TYPE = 'CSV'",
                ""
            ]))
        ])

        resourceName = self.get_standard_inputs()["resource_name"]
        self.assertRegex(result.outs["name"], resourceName + '_[a-f,0-9]{7}')
        self.assertEqual(result.id, result.outs["name"])


    def test_when_give_invalid_db_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())
        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'database': 'invalid-db-name',
        })

    def test_when_give_invalid_schema_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())
        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'schema': 'invalid-schema-name',
        })

    def test_when_give_invalid_name_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())
        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'name': 'invalid-format',
        })

    def test_when_invalid_resource_name_given_and_name_is_autogenerated_then_error_thrown(self):
        mock_connection_provider = self.get_mock_connection_provider(Mock())
        provider = FileFormatProvider(self.get_mock_provider(), mock_connection_provider)

        self.assertRaises(Exception, provider.create, {
            **self.get_standard_inputs(),
            'name': None,
            'resource_name': 'invalid-name'
        })

    # HELPERS

    def get_standard_inputs(self):
        return {
            'database': 'test_database_name',
            'type': 'CSV',
            'resource_name': 'pulumi_test_file_format',
            'name': 'test_file_format',
            'comment': None
        }

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
