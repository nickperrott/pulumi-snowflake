from pulumi.dynamic import CreateResult, DiffResult, ResourceProvider

from pulumi_snowflake.random_id import RandomId
from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.validation import Validation


class AWSStorageIntegrationProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake Storage Integration resources
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__()
        self.connection_provider = connection_provider

    def create(self, inputs):
        connection = self.connection_provider.get()
        cursor = connection.cursor()

        self._require_inputs(inputs, [ 'type', 'storage_provider', 'storage_aws_role_arn', 'enabled',
                               'storage_allowed_locations' ])
        if inputs["name"] is None and inputs["resource_name"] is None:
            raise Exception("At least one of 'name' or 'resource_name' must be provided")

        # Snowflake's input binding only works for column values, not identifiers,
        # so we have to validate them manually and put straight into the SQL
        validated_type = Validation.validate_identifier(inputs["type"])
        validated_storage_provider = Validation.validate_identifier(inputs["storage_provider"])
        validated_name = self._get_validated_name(inputs)
        allowed_locations_placeholder = ','.join(['%s'] * len(inputs['storage_allowed_locations']))

        statements = [
            f"CREATE STORAGE INTEGRATION {validated_name}",
            f"TYPE = {validated_type}",
            f"STORAGE_PROVIDER = {validated_storage_provider}",
            f"STORAGE_AWS_ROLE_ARN = %s",
            f"ENABLED = {self._bool_to_sql(inputs['enabled'])}",
            f"STORAGE_ALLOWED_LOCATIONS = ({allowed_locations_placeholder})"
        ]

        bindings = [
            inputs['storage_aws_role_arn'],
            *inputs['storage_allowed_locations']
        ]

        if inputs.get('comment') is not None:
            statements.append("COMMENT = %s")
            bindings.append(inputs['comment'])

        if inputs.get('storage_blocked_locations') is not None:
            blocked_locations_placeholder = ','.join(['%s'] * len(inputs['storage_blocked_locations']))
            statements.append(f"STORAGE_BLOCKED_LOCATIONS = ({blocked_locations_placeholder})")
            bindings.extend(inputs['storage_blocked_locations'])

        try:
            cursor.execute('\n'.join(statements), (*bindings,))
        finally:
            cursor.close()

        connection.close()

        return CreateResult(id_=validated_name, outs={
            'name': validated_name,
            'type': validated_type,
            'storage_provider': validated_storage_provider,
            'storage_aws_role_arn': inputs["storage_aws_role_arn"],
            'enabled': inputs["enabled"],
            'storage_allowed_locations': inputs["storage_allowed_locations"],
            'storage_blocked_locations': inputs.get("storage_blocked_locations"),
            'comment': inputs.get("comment")
        })

    def _bool_to_sql(self, value):
        if value is None:
            raise Exception("Cannot convert None value to SQL Boolean")

        return 'TRUE' if value else 'FALSE'

    def _require_inputs(self, inputs, keys):
        for key in keys:
            if inputs.get(key) is None:
                raise Exception(f"Required input value '{key}' is not present")

    def _get_validated_name(self, inputs):
        name = inputs.get("name")

        if name is None:
            name = f'{inputs["resource_name"]}_{RandomId.generate(7)}'

        return Validation.validate_identifier(name)
