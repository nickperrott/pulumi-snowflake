from ..client import Client
from ..provider import Provider
from ..baseprovider.base_dynamic_provider import BaseDynamicProvider


class FileFormatProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake FileFormat resources.
    """

    connection_provider: Client

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="File Format")


    def generate_sql_create_statement(self, name, inputs, environment):
        template = environment.from_string(
"""CREATE {{ resource_type | upper }} {{ full_name }}
{% if type %}TYPE = {{ type | sql }}
{% endif %}
{%- if compression %}COMPRESSION = {{ compression | sql }}
{% endif %}
{%- if record_delimiter %}RECORD_DELIMITER = {{ record_delimiter | sql }}
{% endif %}
{%- if field_delimiter %}FIELD_DELIMITER = {{ field_delimiter | sql }}
{% endif %}
{%- if file_extension %}FILE_EXTENSION = {{ file_extension | sql }}
{% endif %}
{%- if skip_header %}SKIP_HEADER = {{ skip_header | sql }}
{% endif %}
{%- if skip_blank_lines is boolean %}SKIP_BLANK_LINES = {{ skip_blank_lines | sql }}
{% endif %}
{%- if date_format %}DATE_FORMAT = {{ date_format | sql }}
{% endif %}
{%- if time_format %}TIME_FORMAT = {{ time_format | sql }}
{% endif %}
{%- if timestamp_format %}TIMESTAMP_FORMAT = {{ timestamp_format | sql }}
{% endif %}
{%- if binary_format %}BINARY_FORMAT = {{ binary_format | sql }}
{% endif %}
{%- if escape %}ESCAPE = {{ escape | sql }}
{% endif %}
{%- if escape_unenclosed_field %}ESCAPE_UNENCLOSED_FIELD = {{ escape_unenclosed_field | sql }}
{% endif %}
{%- if trim_space is boolean %}TRIM_SPACE = {{ trim_space | sql }}
{% endif %}
{%- if field_optionally_enclosed_by %}FIELD_OPTIONALLY_ENCLOSED_BY = {{ field_optionally_enclosed_by | sql }}
{% endif %}
{%- if null_if %}NULL_IF = {{ null_if | sql }}
{% endif %}
{%- if error_on_column_count_mismatch is boolean %}ERROR_ON_COLUMN_COUNT_MISMATCH = {{ error_on_column_count_mismatch | sql }}
{% endif %}
{%- if replace_invalid_characters is boolean %}REPLACE_INVALID_CHARACTERS = {{ replace_invalid_characters | sql }}
{% endif %}
{%- if validate_utf8 is boolean %}VALIDATE_UTF8 = {{ validate_utf8 | sql }}
{% endif %}
{%- if empty_field_as_null is boolean %}EMPTY_FIELD_AS_NULL = {{ empty_field_as_null | sql }}
{% endif %}
{%- if skip_byte_order_mark is boolean %}SKIP_BYTE_ORDER_MARK = {{ skip_byte_order_mark | sql }}
{% endif %}
{%- if encoding %}ENCODING = {{ encoding | sql }}
{% endif %}
{%- if enable_octal is boolean %}ENABLE_OCTAL = {{ enable_octal | sql }}
{% endif %}
{%- if allow_duplicate is boolean %}ALLOW_DUPLICATE = {{ allow_duplicate | sql }}
{% endif %}
{%- if strip_outer_array is boolean %}STRIP_OUTER_ARRAY = {{ strip_outer_array | sql }}
{% endif %}
{%- if strip_null_values is boolean %}STRIP_NULL_VALUES = {{ strip_null_values | sql }}
{% endif %}
{%- if ignore_utf8_errors is boolean %}IGNORE_UTF8_ERRORS = {{ ignore_utf8_errors | sql }}
{% endif %}
{%- if binary_as_text is boolean %}BINARY_AS_TEXT = {{ binary_as_text | sql }}
{% endif %}
{%- if snappy_compression is boolean %}SNAPPY_COMPRESSION = {{ snappy_compression | sql }}
{% endif %}
{%- if preserve_space is boolean %}PRESERVE_SPACE = {{ preserve_space | sql }}
{% endif %}
{%- if strip_outer_element is boolean %}STRIP_OUTER_ELEMENT = {{ strip_outer_element | sql }}
{% endif %}
{%- if disable_snowflake_data is boolean %}DISABLE_SNOWFLAKE_DATA = {{ disable_snowflake_data | sql }}
{% endif %}
{%- if disable_auto_convert is boolean %}DISABLE_AUTO_CONVERT = {{ disable_auto_convert | sql }}
{% endif %}
{%- if comment %}COMMENT = {{ comment | sql }}
{% endif %}""")

        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type,
            **inputs
        })

        return sql

    def generate_sql_drop_statement(self, name, inputs, environment):
        template = environment.from_string("DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type,
        })
        return sql
