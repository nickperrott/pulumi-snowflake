from typing import Optional, List

from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import Resource

from ..provider import Provider
from ..client import Client
from .file_format_provider import FileFormatProvider


class FileFormat(Resource):
    """
    Represents a Snowflake File Format.  See
    https://docs.snowflake.net/manuals/sql-reference/sql/create-file-format.html
    for more details of parameters.
    """

    name: Output[str]
    """
    The name of the file format in Snowflake.
    """

    full_name: Output[str]
    """
    The fully-qualified name of the file format in Snowflake, including database and schema.
    """

    type: Output[str]
    """
    The file format type.  One of `FileFormatType`.
    """

    database: Output[str]
    """
    The Snowflake database in which the file format exists.
    """

    schema: Output[str]
    """
    The Snowflake schema in which the file format exists.
    """

    full_name: Output[str]
    """
    The fully qualified name of the resource.
    """

    def __init__(self,
                 resource_name: str,
                 database: Input[str] = None,
                 type: Input[str] = None,
                 compression: Input[Optional[str]] = None,
                 record_delimiter: Input[Optional[str]] = None,
                 field_delimiter: Input[Optional[str]] = None,
                 file_extension: Input[Optional[str]] = None,
                 skip_header: Input[Optional[int]] = None,
                 skip_blank_lines: Input[Optional[bool]] = None,
                 date_format: Input[Optional[str]] = None,
                 time_format: Input[Optional[str]] = None,
                 timestamp_format: Input[Optional[str]] = None,
                 binary_format: Input[Optional[str]] = None,
                 escape: Input[Optional[str]] = None,
                 escape_unenclosed_field: Input[Optional[str]] = None,
                 trim_space: Input[Optional[bool]] = None,
                 field_optionally_enclosed_by: Input[Optional[str]] = None,
                 null_if: Input[Optional[List[str]]] = None,
                 error_on_column_count_mismatch: Input[Optional[bool]] = None,
                 replace_invalid_characters: Input[Optional[bool]] = None,
                 validate_utf8: Input[Optional[bool]] = None,
                 empty_field_as_null: Input[Optional[bool]] = None,
                 skip_byte_order_mark: Input[Optional[bool]] = None,
                 encoding: Input[Optional[str]] = None,
                 enable_octal: Input[Optional[bool]] = None,
                 allow_duplicate: Input[Optional[bool]] = None,
                 strip_outer_array: Input[Optional[bool]] = None,
                 strip_null_values: Input[Optional[bool]] = None,
                 ignore_utf8_errors: Input[Optional[bool]] = None,
                 binary_as_text: Input[Optional[bool]] = None,
                 snappy_compression: Input[Optional[bool]] = None,
                 preserve_space: Input[Optional[bool]] = None,
                 strip_outer_element: Input[Optional[bool]] = None,
                 disable_snowflake_data: Input[Optional[bool]] = None,
                 disable_auto_convert: Input[Optional[bool]] = None,
                 comment: Input[Optional[str]] = None,
                 name: Input[str] = None,
                 schema: Input[str] = None,
                 provider: Provider = None,
                 opts: Optional[ResourceOptions] = None):
        provider = provider if provider else Provider()
        client = Client(provider=provider)
        super().__init__(FileFormatProvider(provider, client), resource_name, {
            'database': database,
            'resource_name': resource_name,
            'full_name': None,
            'compression': compression,
            'record_delimiter': record_delimiter,
            'field_delimiter': field_delimiter,
            'file_extension': file_extension,
            'skip_header': skip_header,
            'skip_blank_lines': skip_blank_lines,
            'date_format': date_format,
            'time_format': time_format,
            'timestamp_format': timestamp_format,
            'binary_format': binary_format,
            'escape': escape,
            'escape_unenclosed_field': escape_unenclosed_field,
            'trim_space': trim_space,
            'field_optionally_enclosed_by': field_optionally_enclosed_by,
            'null_if': null_if,
            'error_on_column_count_mismatch': error_on_column_count_mismatch,
            'replace_invalid_characters': replace_invalid_characters,
            'validate_utf8': validate_utf8,
            'empty_field_as_null': empty_field_as_null,
            'skip_byte_order_mark': skip_byte_order_mark,
            'encoding': encoding,
            'enable_octal': enable_octal,
            'allow_duplicate': allow_duplicate,
            'strip_outer_array': strip_outer_array,
            'strip_null_values': strip_null_values,
            'ignore_utf8_errors': ignore_utf8_errors,
            'binary_as_text': binary_as_text,
            'snappy_compression': snappy_compression,
            'preserve_space': preserve_space,
            'strip_outer_element': strip_outer_element,
            'disable_snowflake_data': disable_snowflake_data,
            'disable_auto_convert': disable_auto_convert,
            'comment': comment,
            'name': name,
            'full_name': None,
            'type': type,
            'schema': schema
        }, opts)
