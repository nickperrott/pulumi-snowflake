import unittest

from pulumi_snowflake import CompressionValues, AutoToken, NoneToken, BinaryFormatValues
from pulumi_snowflake.fileformat import FileFormatType
from pulumi_snowflake.stage import StageFileFormat


class StageFormatOptionsTests(unittest.TestCase):

    def test_when_pass_values_then_generates_dict(self):
        self.maxDiff = None
        format_options = StageFileFormat(
            format_name="test-format-name",
            type=FileFormatType.AVRO,
            compression=CompressionValues.GZIP,
            record_delimiter=':',
            field_delimiter=NoneToken(),
            file_extension='csv',
            skip_header=True,
            skip_blank_lines=False,
            date_format=AutoToken(),
            time_format='hhmm',
            timestamp_format=AutoToken(),
            binary_format=BinaryFormatValues.BASE64,
            escape="/",
            escape_unenclosed_field=NoneToken(),
            trim_space=True,
            field_optionally_enclosed_by=NoneToken(),
            null_if=["N", "NULL"],
            error_on_column_count_mismatch=False,
            validate_utf8=True,
            empty_field_as_null=False,
            skip_byte_order_mark=True,
            encoding='UTF-8',
            disable_snowflake_data=True,
            strip_null_values=False,
            strip_outer_element=True,
            strip_outer_array=False,
            enable_octal=True,
            preserve_space=False,
            snappy_compression=True,
            ignore_utf8_errors=False,
            allow_duplicate=True,
            disable_auto_convert=False,
            binary_as_text=True,
        )
        actual = format_options.as_dict()
        expected = {
            "format_name": "test-format-name",
            "type": FileFormatType.AVRO,
            "compression": CompressionValues.GZIP,
            "record_delimiter": ':',
            "field_delimiter": NoneToken(),
            "file_extension": 'csv',
            "skip_header": True,
            "skip_blank_lines": False,
            "date_format": AutoToken(),
            "time_format": 'hhmm',
            "timestamp_format": AutoToken(),
            "binary_format": BinaryFormatValues.BASE64,
            "escape": "/",
            "escape_unenclosed_field": NoneToken(),
            "trim_space": True,
            "field_optionally_enclosed_by": NoneToken(),
            "null_if": ["N", "NULL"],
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
        }
        self.assertDictEqual(expected, actual)