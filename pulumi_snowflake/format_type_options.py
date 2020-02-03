from typing import Optional, Union, List

from pulumi import Input


class CompressionValues:
    AUTO = "AUTO"
    GZIP = "GZIP"
    BZ2 = "BZ2"
    BROTLI = "BROTLI"
    ZSTD = "ZSTD"
    DEFLATE = "DEFLATE"
    RAW_DEFLATE = "RAW_DEFLATE"
    NONE = "NONE"

class BinaryFormatValues:
    HEX = "HEX"
    BASE64 = "BASE64"
    UTF8 = "UTF8"


class NoneValue:
    pass

def eq_is_none(self, other):
    return isinstance(other, NoneValue)

NoneValue.__eq__ = eq_is_none


class AutoValue:
    pass

def eq_is_auto(self, other):
    return isinstance(other, AutoValue)

AutoValue.__eq__ = eq_is_auto



class StageFormatTypeOptions:
    pass

class StageCsvFormatTypeOptions:
    def __init__(self,
                 compression: Input[Optional[str]] = None,
                 record_delimiter: Input[Optional[Union[str, NoneValue]]] = None,
                 field_delimiter: Input[Optional[Union[str, NoneValue]]] = None,
                 file_extension: Input[Optional[Union[str, NoneValue]]] = None,
                 skip_header: Input[Optional[int]] = None,
                 skip_blank_lines: Input[Optional[bool]] = None,
                 date_format: Input[Optional[Union[str, AutoValue]]] = None,
                 time_format: Input[Optional[Union[str, AutoValue]]] = None,
                 timestamp_format: Input[Optional[Union[str, AutoValue]]] = None,
                 binary_format: Input[Optional[str]] = None,
                 escape: Input[Optional[Union[str, NoneValue]]] = None,
                 escape_unenclosed_field: Input[Optional[Union[str, NoneValue]]] = None,
                 trim_space: Input[Optional[bool]] = None,
                 field_optionally_enclosed_by: Input[Optional[Union[str, NoneValue]]] = None,
                 null_if: Input[Optional[List[str]]] = None,
                 error_on_column_count_mismatch: Input[Optional[bool]] = None,
                 validate_utf8: Input[Optional[bool]] = None,
                 empty_field_as_null: Input[Optional[bool]] = None,
                 skip_byte_order_mark: Input[Optional[bool]] = None,
                 encoding: Input[Optional[str]] = None,
                 ):
        """
        :param pulumi.Input[Optional[str]] compression: String (constant) that specifies the current compression
            algorithm for the data files to be loaded.  Should be one of `CompressionValues`
        :param pulumi.Input[Optional[Union[str, NoneValue]]] record_delimiter: One or more singlebyte or multibyte
            characters that separate records in an input file (data loading) or unloaded file (data unloading).
        :param pulumi.Input[Optional[Union[str, NoneValue]]] field_delimiter: One or more singlebyte or multibyte
            characters that separate fields in an input file (data loading) or unloaded file (data unloading),
        :param pulumi.Input[Optional[Union[str, NoneValue]]] file_extension: Specifies the extension for files unloaded
            to a stage. Accepts any extension. The user is responsible for specifying a file extension that can be read
            by any desired software or services.
        :param pulumi.Input[Optional[int]] skip_header: Number of lines at the start of the file to skip.
        :param pulumi.Input[Optional[bool]] skip_blank_lines: Boolean that specifies to skip any blank lines encountered
            in the data files; otherwise, blank lines produce an end-of-record error (default behavior).,
        :param pulumi.Input[Optional[Union[str, AutoValue]]] date_format: Defines the format of date values in the data
            files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[Union[str, AutoValue]]] time_format: Defines the format of time values in the data
            files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[Union[str, AutoValue]]] timestamp_format: Defines the format of timestamp values in
            the data files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[str]] binary_format: Defines the encoding format for binary input or output.
        :param pulumi.Input[Optional[Union[str, NoneValue]]] escape: Single character string used as the escape
            character for any field values.  Should be one of `BinaryFormatValues`.
        :param pulumi.Input[Optional[Union[str, NoneValue]]] escape_unenclosed_field: Single character string used as
            the escape character for unenclosed field values only.
        :param pulumi.Input[Optional[bool]] trim_space: Boolean that specifies whether to remove white space from
            fields.
        :param pulumi.Input[Optional[Union[str, NoneValue]]] field_optionally_enclosed_by: Character used to enclose
            strings.
        :param pulumi.Input[Optional[List[str]]] null_if: String used to convert to and from SQL NULL.
        :param pulumi.Input[Optional[bool]] error_on_column_count_mismatch: Boolean that specifies whether to generate a
            parsing error if the number of delimited columns (i.e. fields) in an input file does not match the number of
            columns in the corresponding table.
        :param pulumi.Input[Optional[bool]] validate_utf8: Boolean that specifies whether to validate UTF-8 character
            encoding in string column data.
        :param pulumi.Input[Optional[bool]] empty_field_as_null: When loading data, specifies whether to insert SQL NULL
            for empty fields in an input file, which are represented by two successive delimiters (e.g. ,,)
        :param pulumi.Input[Optional[bool]] skip_byte_order_mark:  Boolean that specifies whether to skip the BOM (byte
            order mark), if present in a data file.
        :param pulumi.Input[Optional[str]] encoding: String (constant) that specifies the character set of the source
            data when loading data into a table.
        """
        self.compression = compression
        self.record_delimiter = record_delimiter
        self.field_delimiter = field_delimiter
        self.file_extension = file_extension
        self.skip_header = skip_header
        self.skip_blank_lines = skip_blank_lines
        self.date_format = date_format
        self.time_format = time_format
        self.timestamp_format = timestamp_format
        self.binary_format = binary_format
        self.escape = escape
        self.escape_unenclosed_field = escape_unenclosed_field
        self.trim_space = trim_space
        self.field_optionally_enclosed_by = field_optionally_enclosed_by
        self.null_if = null_if
        self.error_on_column_count_mismatch = error_on_column_count_mismatch
        self.validate_utf8 = validate_utf8
        self.empty_field_as_null = empty_field_as_null
        self.skip_byte_order_mark = skip_byte_order_mark
        self.encoding = encoding


    def as_dict(self):
        fields = [
            "compression",
            "record_delimiter",
            "field_delimiter",
            "file_extension",
            "skip_header",
            "skip_blank_lines",
            "date_format",
            "time_format",
            "timestamp_format",
            "binary_format",
            "escape",
            "escape_unenclosed_field",
            "trim_space",
            "field_optionally_enclosed_by",
            "null_if",
            "error_on_column_count_mismatch",
            "validate_utf8",
            "empty_field_as_null",
            "skip_byte_order_mark",
            "encoding"
        ]
        return {field: getattr(self, field) for field in fields}