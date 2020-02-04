import unittest
from unittest.mock import Mock, call

from pulumi_snowflake import CompressionValues, NoneValue, AutoValue, BinaryFormatValues, StageOnCopyErrorValues, \
    StageMatchByColumnNameValues
from pulumi_snowflake.fileformat import FileFormatType
from pulumi_snowflake.stage import StageProvider
from test.on_copy_error_values import OnCopyErrorValuesTests


class StageTests(unittest.TestCase):

    def test_create_stage(self):

        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StageProvider(mock_connection_provider)
        provider.create({
            "file_format": {
                'format_name': 'test_file_format',
                'type': None
            },
            "comment": "test_comment",
            "name": "test_stage",
            "database": "test_database",
            "schema": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STAGE test_database.test_schema.test_stage",
                f"FILE_FORMAT = (FORMAT_NAME = %s)",
                f"COMMENT = %s"
            ]), ('test_file_format', 'test_comment'))
        ])


    def test_when_file_format_given_then_appears_in_sql(self):

        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StageProvider(mock_connection_provider)
        provider.create({
            "file_format": {
                "format_name": "test-format-name",
                "type": FileFormatType.AVRO,
                "compression": CompressionValues.GZIP,
                "record_delimiter": ':',
                "field_delimiter": NoneValue(),
                "file_extension": 'csv',
                "skip_header": 100,
                "skip_blank_lines": False,
                "date_format": AutoValue(),
                "time_format": 'hhmm',
                "timestamp_format": AutoValue(),
                "binary_format": BinaryFormatValues.BASE64,
                "escape": "/",
                "escape_unenclosed_field": NoneValue(),
                "trim_space": True,
                "field_optionally_enclosed_by": NoneValue(),
                "null_if": ["N","NULL"],
                "error_on_column_count_mismatch": False,
                "validate_utf8": True,
                "empty_field_as_null": False,
                "skip_byte_order_mark": True,
                "encoding": 'UTF-8',
                "disable_snowflake_data": True,
                "strip_null_values": False,
                "strip_outer_element": True,
                "strip_outer_array": False,
                "enable_octal": True,
                "preserve_space": False,
                "snappy_compression": True,
                "ignore_utf8_errors": False,
                "allow_duplicate": True,
                "disable_auto_convert": False,
                "binary_as_text": True,
            },
            "comment": "test_comment",
            "name": "test_stage",
            "database": "test_database",
            "schema": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STAGE test_database.test_schema.test_stage",
                ", ".join([
                    f"FILE_FORMAT = (FORMAT_NAME = %s",
                    f"TYPE = AVRO",
                    f"COMPRESSION = GZIP",
                    f"RECORD_DELIMITER = %s",
                    f"FIELD_DELIMITER = NONE",
                    f"FILE_EXTENSION = %s",
                    f"SKIP_HEADER = 100",
                    f"SKIP_BLANK_LINES = FALSE",
                    f"DATE_FORMAT = AUTO",
                    f"TIME_FORMAT = %s",
                    f"TIMESTAMP_FORMAT = AUTO",
                    f"BINARY_FORMAT = BASE64",
                    f"ESCAPE = %s",
                    f"ESCAPE_UNENCLOSED_FIELD = NONE",
                    f"TRIM_SPACE = TRUE",
                    f"FIELD_OPTIONALLY_ENCLOSED_BY = NONE",
                    f"NULL_IF = (%s,%s)",
                    f"ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE",
                    f"VALIDATE_UTF8 = TRUE",
                    f"EMPTY_FIELD_AS_NULL = FALSE",
                    f"SKIP_BYTE_ORDER_MARK = TRUE",
                    f"ENCODING = %s",
                    f"DISABLE_SNOWFLAKE_DATA = TRUE",
                    f"STRIP_NULL_VALUES = FALSE",
                    f"STRIP_OUTER_ELEMENT = TRUE",
                    f"STRIP_OUTER_ARRAY = FALSE",
                    f"ENABLE_OCTAL = TRUE",
                    f"PRESERVE_SPACE = FALSE",
                    f"SNAPPY_COMPRESSION = TRUE",
                    f"IGNORE_UTF8_ERRORS = FALSE",
                    f"ALLOW_DUPLICATE = TRUE",
                    f"DISABLE_AUTO_CONVERT = FALSE",
                    f"BINARY_AS_TEXT = TRUE)",
                ]),
                f"COMMENT = %s"
            ]), (
                    "test-format-name",
                    ':',
                    'csv',
                    'hhmm',
                    "/",
                    "N", "NULL",
                    'UTF-8',
                     'test_comment',
                )
            )
        ])


    def test_when_copy_options_given_then_appears_in_sql(self):

        mock_cursor = Mock()
        mock_connection_provider = self.get_mock_connection_provider(mock_cursor)

        provider = StageProvider(mock_connection_provider)
        provider.create({
            "file_format": None,
            "copy_options":{
                "on_error": StageOnCopyErrorValues.skip_file_percent(45),
                "size_limit": 345,
                "purge": True,
                "return_failed_only": False,
                "match_by_column_name": StageMatchByColumnNameValues.CASE_INSENSITIVE,
                "enforce_length": True,
                "truncatecolumns": False,
                "force": True,
            },
            "comment": "test_comment",
            "name": "test_stage",
            "database": "test_database",
            "schema": "test_schema"
        })

        mock_cursor.execute.assert_has_calls([
            call("\n".join([
                f"CREATE STAGE test_database.test_schema.test_stage",
                ", ".join([
                    f"COPY_OPTIONS = (ON_ERROR = SKIP_FILE_45%",
                    f"SIZE_LIMIT = 345",
                    f"PURGE = TRUE",
                    f"RETURN_FAILED_ONLY = FALSE",
                    f"MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE",
                    f"ENFORCE_LENGTH = TRUE",
                    f"TRUNCATECOLUMNS = FALSE",
                    f"FORCE = TRUE)",
                ]),
                f"COMMENT = %s"
            ]), ('test_comment',)
            )
        ])



    # HELPERS

    def get_mock_connection_provider(self, mock_cursor):
        mockConnection = Mock()
        mockConnection.cursor.return_value = mock_cursor
        mock_connection_provider = Mock()
        mock_connection_provider.get.return_value = mockConnection
        return mock_connection_provider
