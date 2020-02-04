from pulumi_snowflake import ConnectionProvider
from pulumi_snowflake.provider import StringAttribute, IdentifierAttribute, StructAttribute, Provider, BooleanAttribute, \
    StringListAttribute
from pulumi_snowflake.provider.attribute.integer_attribute import IntegerAttribute
from pulumi_snowflake.provider.attribute.value_or_auto_attribute import ValueOrAutoAttribute
from pulumi_snowflake.provider.attribute.value_or_none_attribute import ValueOrNoneAttribute
from pulumi_snowflake.provider.attribute.value_or_token_attribute import ValueOrTokenAttribute
from pulumi_snowflake.utf8_token import UTF8Token
from pulumi_snowflake.validation import Validation


class StageProvider(Provider):
    """
    Dynamic provider for Snowflake Stage resources.
    """

    def __init__(self, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "STAGE", [
            StringAttribute("url"),
            IdentifierAttribute("storage_integration"),
            StructAttribute("credentials", False, [
                StringAttribute("aws_key_id"),
                StringAttribute("aws_secret_key"),
                StringAttribute("aws_token"),
                StringAttribute("aws_role"),
                StringAttribute("azure_sas_token"),
            ]),
            StructAttribute("encryption", False, [
                ValueOrNoneAttribute(StringAttribute("type")),
                StringAttribute("master_key"),
                StringAttribute("kms_key_id"),
            ]),
            StructAttribute("file_format", False, [
                StringAttribute("format_name"),
                IdentifierAttribute("type"),
                IdentifierAttribute("compression"),
                ValueOrNoneAttribute(StringAttribute("record_delimiter")),
                ValueOrNoneAttribute(StringAttribute("field_delimiter")),
                StringAttribute("file_extension"),
                IntegerAttribute("skip_header"),
                BooleanAttribute("skip_blank_lines"),
                ValueOrAutoAttribute(StringAttribute("date_format")),
                ValueOrAutoAttribute(StringAttribute("time_format")),
                ValueOrAutoAttribute(StringAttribute("timestamp_format")),
                IdentifierAttribute("binary_format"),
                ValueOrNoneAttribute(StringAttribute("escape")),
                ValueOrNoneAttribute(StringAttribute("escape_unenclosed_field")),
                BooleanAttribute("trim_space"),
                ValueOrNoneAttribute(StringAttribute("field_optionally_enclosed_by")),
                StringListAttribute("null_if"),
                BooleanAttribute("error_on_column_count_mismatch"),
                BooleanAttribute("validate_utf8"),
                BooleanAttribute("empty_field_as_null"),
                BooleanAttribute("skip_byte_order_mark"),
                ValueOrTokenAttribute(StringAttribute("encoding"), UTF8Token()),
                BooleanAttribute("disable_snowflake_data"),
                BooleanAttribute("strip_null_values"),
                BooleanAttribute("strip_outer_element"),
                BooleanAttribute("strip_outer_array"),
                BooleanAttribute("enable_octal"),
                BooleanAttribute("preserve_space"),
                BooleanAttribute("snappy_compression"),
                BooleanAttribute("ignore_utf8_errors"),
                BooleanAttribute("allow_duplicate"),
                BooleanAttribute("disable_auto_convert"),
                BooleanAttribute("binary_as_text"),
            ]),
            StructAttribute("copy_options", False, [
                IdentifierAttribute("on_error"),
                IntegerAttribute("size_limit"),
                BooleanAttribute("purge"),
                BooleanAttribute("return_failed_only"),
                IdentifierAttribute("match_by_column_name"),
                BooleanAttribute("enforce_length"),
                BooleanAttribute("truncatecolumns"),
                BooleanAttribute("force"),
            ]),
            StringAttribute("comment", False)
        ],
        [
            "temporary"
        ])

    def generate_outputs(self, name, inputs, outs):
        """
        Appends the schema name and database name to the outputs
        """
        return {
            "database": inputs["database"],
            "schema": inputs.get("schema"),
            **outs
        }

    def get_full_object_name(self, validated_name, inputs):
        """
        For objects which are scoped to a schema, the full qualified object name is in the form 'database.schema.name',
        where schema can be empty if the default schema is required.
        """
        validated_database = Validation.validate_identifier(inputs["database"])
        validated_schema = self._get_validated_schema_or_none(inputs)

        return f"{validated_database}.{validated_schema}.{validated_name}" \
            if validated_schema is not None else \
            f"{validated_database}..{validated_name}"

    def _get_validated_schema_or_none(self, inputs):
        schema = inputs.get("schema")

        if schema is not None:
            return Validation.validate_identifier(schema)

        return None

