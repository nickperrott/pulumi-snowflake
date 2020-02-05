from typing import Optional, Union, List

from pulumi import Input

from ..auto_token import AutoToken
from ..none_token import NoneToken


class StageFileFormat:
    """
    Represents the file format options used when creating a stage.
    """
    def __init__(self,
                 format_name: Input[Optional[str]] = None,
                 type: Input[Optional[str]] = None,
                 compression: Input[Optional[str]] = None,
                 record_delimiter: Input[Optional[Union[str, NoneToken]]] = None,
                 field_delimiter: Input[Optional[Union[str, NoneToken]]] = None,
                 file_extension: Input[Optional[Union[str, NoneToken]]] = None,
                 skip_header: Input[Optional[int]] = None,
                 skip_blank_lines: Input[Optional[bool]] = None,
                 date_format: Input[Optional[Union[str, AutoToken]]] = None,
                 time_format: Input[Optional[Union[str, AutoToken]]] = None,
                 timestamp_format: Input[Optional[Union[str, AutoToken]]] = None,
                 binary_format: Input[Optional[str]] = None,
                 escape: Input[Optional[Union[str, NoneToken]]] = None,
                 escape_unenclosed_field: Input[Optional[Union[str, NoneToken]]] = None,
                 trim_space: Input[Optional[bool]] = None,
                 field_optionally_enclosed_by: Input[Optional[Union[str, NoneToken]]] = None,
                 null_if: Input[Optional[List[str]]] = None,
                 error_on_column_count_mismatch: Input[Optional[bool]] = None,
                 validate_utf8: Input[Optional[bool]] = None,
                 empty_field_as_null: Input[Optional[bool]] = None,
                 skip_byte_order_mark: Input[Optional[bool]] = None,
                 encoding: Input[Optional[str]] = None,
                 enable_octal: Input[Optional[bool]] = None,
                 allow_duplicate: Input[Optional[bool]] = None,
                 strip_outer_array: Input[Optional[bool]] = None,
                 strip_null_values: Input[Optional[bool]] = None,
                 ignore_utf8_errors: Input[Optional[bool]] = None,
                 snappy_compression: Input[Optional[bool]] = None,
                 binary_as_text: Input[Optional[bool]] = None,
                 preserve_space: Input[Optional[bool]] = None,
                 strip_outer_element: Input[Optional[bool]] = None,
                 disable_snowflake_data: Input[Optional[bool]] = None,
                 disable_auto_convert: Input[Optional[bool]] = None,
                 ):
        """
        :param pulumi.Input[Optional[str]] format_name: Specifies an existing named file format to use for the stage.
        :param pulumi.Input[Optional[str]] type: Specifies the type of files for the stage.  Should be one of
            `FileFormatType`.
        :param pulumi.Input[Optional[str]] compression: String (constant) that specifies the current compression
            algorithm for the data files to be loaded.  Should be one of `CompressionValues`
        :param pulumi.Input[Optional[Union[str, NoneToken]]] record_delimiter: One or more singlebyte or multibyte
            characters that separate records in an input file (data loading) or unloaded file (data unloading).
        :param pulumi.Input[Optional[Union[str, NoneToken]]] field_delimiter: One or more singlebyte or multibyte
            characters that separate fields in an input file (data loading) or unloaded file (data unloading),
        :param pulumi.Input[Optional[Union[str,NoneToken]]] file_extension: Specifies the extension for files unloaded
            to a stage. Accepts any extension. The user is responsible for specifying a file extension that can be read
            by any desired software or services.
        :param pulumi.Input[Optional[int]] skip_header: Number of lines at the start of the file to skip.
        :param pulumi.Input[Optional[bool]] skip_blank_lines: Boolean that specifies to skip any blank lines encountered
            in the data files; otherwise, blank lines produce an end-of-record error (default behavior).,
        :param pulumi.Input[Optional[Union[str, AutoToken]]] date_format: Defines the format of date values in the data
            files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[Union[str, AutoToken]]] time_format: Defines the format of time values in the data
            files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[Union[str, AutoToken]]] timestamp_format: Defines the format of timestamp values in
            the data files (data loading) or table (data unloading).
        :param pulumi.Input[Optional[str]] binary_format: Defines the encoding format for binary input or output.
        :param pulumi.Input[Optional[Union[str, NoneToken]]] escape: Single character string used as the escape
            character for any field values.  Should be one of `BinaryFormatValues`.
        :param pulumi.Input[Optional[Union[str, NoneToken]]] escape_unenclosed_field: Single character string used as
            the escape character for unenclosed field values only.
        :param pulumi.Input[Optional[bool]] trim_space: Boolean that specifies whether to remove white space from
            fields.
        :param pulumi.Input[Optional[Union[str, NoneToken]]] field_optionally_enclosed_by: Character used to enclose
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
        :param pulumi.Input[Optional[bool]] enable_octal: Boolean that enables parsing of octal numbers.
        :param pulumi.Input[Optional[bool]] allow_duplicate: Boolean that specifies to allow duplicate object field
            names (only the last one will be preserved).
        :param pulumi.Input[Optional[bool]] strip_outer_array: Boolean that instructs the JSON parser to remove outer
            brackets (i.e `[ ]`).
        :param pulumi.Input[Optional[bool]] strip_null_values: Boolean that instructs the JSON parser to remove object
            fields or array elements containing null values.
        :param pulumi.Input[Optional[bool]] ignore_utf8_errors: Boolean that specifies whether UTF-8 encoding errors
            produce error conditions.
        :param pulumi.Input[Optional[bool]] snappy_compression: Boolean that specifies whether unloaded file(s) are
            compressed using the SNAPPY algorithm.
        :param pulumi.Input[Optional[bool]] binary_as_text: Boolean that specifies whether to interpret columns with no
            defined logical data type as UTF-8 text.
        :param pulumi.Input[Optional[bool]] preserve_space: Boolean that specifies whether the XML parser preserves
            leading and trailing spaces in element content.
        :param pulumi.Input[Optional[bool]] strip_outer_element: Boolean that specifies whether the XML parser strips
            out the outer XML element, exposing 2nd level elements as separate documents.
        :param pulumi.Input[Optional[bool]] disable_snowflake_data: Boolean that specifies whether the XML parser
            disables recognition of Snowflake semi-structured data tags.
        :param pulumi.Input[Optional[bool]] disable_auto_convert: Boolean that specifies whether the XML parser disables
            automatic conversion of numeric and Boolean values from text to native representation.
        """
        super().__init__()
        self.format_name = format_name
        self.type = type
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
        self.enable_octal = enable_octal
        self.allow_duplicate = allow_duplicate
        self.strip_outer_array = strip_outer_array
        self.strip_null_values = strip_null_values
        self.ignore_utf8_errors = ignore_utf8_errors
        self.snappy_compression = snappy_compression
        self.binary_as_text = binary_as_text
        self.preserve_space = preserve_space
        self.strip_outer_element = strip_outer_element
        self.disable_snowflake_data = disable_snowflake_data
        self.disable_auto_convert = disable_auto_convert


    def as_dict(self):
        fields = [
            "format_name",
            "type",
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
            "encoding",
            "enable_octal",
            "allow_duplicate",
            "strip_outer_array",
            "strip_null_values",
            "ignore_utf8_errors",
            "snappy_compression",
            "binary_as_text",
            "preserve_space",
            "strip_outer_element",
            "disable_snowflake_data",
            "disable_auto_convert",
        ]
        return {field: getattr(self, field) for field in fields}
