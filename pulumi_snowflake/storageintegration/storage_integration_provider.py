from typing import List


from pulumi.dynamic import CreateResult, ResourceProvider

from pulumi_snowflake.random_id import RandomId
from pulumi_snowflake import SnowflakeConnectionProvider
from pulumi_snowflake.snowflakeprovider import SnowflakeObjectAttribute, IdentifierAttribute, StringAttribute
from pulumi_snowflake.snowflakeprovider.boolean_attribute import BooleanAttribute
from pulumi_snowflake.snowflakeprovider.string_list_attribute import StringListAttribute
from pulumi_snowflake.validation import Validation


class AWSStorageIntegrationProvider(ResourceProvider):
    """
    Dynamic provider for Snowflake Storage Integration resources
    """

    connection_provider: SnowflakeConnectionProvider

    def __init__(self, connection_provider: SnowflakeConnectionProvider):
        super().__init__()
        self.connection_provider = connection_provider

        self.attributes: List[SnowflakeObjectAttribute] = [
            IdentifierAttribute("type", True),
            IdentifierAttribute("storage_provider", True),
            StringAttribute("storage_aws_role_arn", True),
            BooleanAttribute("enabled", True),
            StringListAttribute("storage_allowed_locations", True),
            StringListAttribute("storage_blocked_locations", False),
            StringAttribute("comment", False)
        ]



    def create(self, inputs):
        self.check_required_attributes(inputs)
        validated_name = self._get_validated_name(inputs)
        attributesWithValues = list(filter(lambda a: inputs.get(a.name) is not None, self.attributes))

        sqlStatements = self.generate_sql_create_statement(attributesWithValues, validated_name, inputs)
        sqlBindings = self.generate_sql_create_bindings(attributesWithValues, inputs)
        self.execute_sql(sqlStatements, sqlBindings)

        return CreateResult(id_=validated_name, outs={
            'name': validated_name,
            **self.generate_outputs(inputs)
        })

    def execute_sql(self, statements, bindings):
        connection = self.connection_provider.get()
        cursor = connection.cursor()
        try:
            cursor.execute('\n'.join(statements), (*bindings,))
        finally:
            cursor.close()
        connection.close()

    def generate_outputs(self, inputs):
        outputs = {a.name: inputs.get(a.name) for a in self.attributes}
        return outputs

    def generate_sql_create_bindings(self, attributesWithValues, inputs):
        bindingTuplesList = list(map(lambda a: a.generate_bindings(inputs.get(a.name)), attributesWithValues))
        bindingTuplesList = filter(lambda t: t is not None, bindingTuplesList)
        bindings = [item for sublist in bindingTuplesList for item in sublist]
        return bindings

    def generate_sql_create_statement(self, attributesWithValues, validated_name, inputs):
        statements = [
            f"CREATE STORAGE INTEGRATION {validated_name}",
            *list(map(lambda a: a.generate_sql(inputs.get(a.name)), attributesWithValues))
        ]
        return statements

    def check_required_attributes(self, inputs):
        for attribute in self.attributes:
            if attribute.is_required() and inputs[attribute.name] is None:
                raise Exception(f"Required input attribute '{attribute.name}' is not present")
        if inputs["name"] is None and inputs["resource_name"] is None:
            raise Exception("At least one of 'name' or 'resource_name' must be provided")

    def _get_validated_name(self, inputs):
        name = inputs.get("name")

        if name is None:
            name = f'{inputs["resource_name"]}_{RandomId.generate(7)}'

        return Validation.validate_identifier(name)
