from pulumi_snowflake.snowflakeprovider.snowflake_object_provider import SnowflakeObjectProvider


class GloballyScopedObjectProvider(SnowflakeObjectProvider):
    """
    A Pulumi dynamic provider which manages a globally scoped (i.e., belonging to the entire account, not a specific
    schema) Snowflake object.  Objects are described by passing in the SQL name of the object (e.g.,
    "STORAGE INTEGRATION) and a list of attributes represented as `SnowflakeObjectAttribute` instances.  This class then
    automatically handles the create, delete and diff methods by generating and executing the appropriate SQL commands.
    """

    def get_full_object_name(self, validated_name, inputs):
        """
        For globally scoped objects, objects belong to the account so do not need further qualification.
        """
        return validated_name

    def generate_outputs(self, name, inputs, outs):
        """
        Nothing to add to outputs.
        """
        return outs