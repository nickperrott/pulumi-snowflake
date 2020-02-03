import unittest

from pulumi_snowflake import CompressionValues, NoneValue, AutoValue, BinaryFormatValues
from pulumi_snowflake.stage import StageCsvFileFormat


class StageFormatOptionsTests(unittest.TestCase):

    def test_when_pass_csv_values_then_generates_dict(self):
        self.maxDiff = None
        format_options = StageCsvFileFormat(
            compression=CompressionValues.GZIP,
            record_delimiter=':',
            field_delimiter=NoneValue(),
            file_extension='csv',
            skip_header=True,
            skip_blank_lines=False,
            date_format=AutoValue(),
            time_format='hhmm',
            timestamp_format=AutoValue(),
            binary_format=BinaryFormatValues.BASE64,
            escape="/",
            escape_unenclosed_field=NoneValue(),
            trim_space=True,
            field_optionally_enclosed_by=NoneValue(),
            null_if=["N", "NULL"],
            error_on_column_count_mismatch=False,
            validate_utf8=True,
            empty_field_as_null=False,
            skip_byte_order_mark=True,
            encoding='UTF-8'
        )
        self.assertDictEqual(format_options.as_dict(), {
            "compression": CompressionValues.GZIP,
            "record_delimiter": ':',
            "field_delimiter": NoneValue(),
            "file_extension": 'csv',
            "skip_header": True,
            "skip_blank_lines": False,
            "date_format": AutoValue(),
            "time_format": 'hhmm',
            "timestamp_format": AutoValue(),
            "binary_format": BinaryFormatValues.BASE64,
            "escape": "/",
            "escape_unenclosed_field": NoneValue(),
            "trim_space": True,
            "field_optionally_enclosed_by": NoneValue(),
            "null_if": ["N", "NULL"],
            "error_on_column_count_mismatch": False,
            "validate_utf8": True,
            "empty_field_as_null": False,
            "skip_byte_order_mark": True,
            "encoding": 'UTF-8'
        })