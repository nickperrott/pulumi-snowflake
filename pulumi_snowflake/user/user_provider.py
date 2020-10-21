from typing import List
from .. import Client
from ..baseprovider import BaseDynamicProvider
from ..provider import Provider
from ..validation import Validation


class UserProvider(BaseDynamicProvider):
    """
    Dynamic provider for Snowflake USer resources.
    """

    def __init__(self, provider_params: Provider, connection_provider: Client):
        super().__init__(provider_params, connection_provider, resource_type="User")

    def generate_sql_create_statement(self, name, inputs, environment):
        sql = []
        template = environment.from_string(
            """CREATE {{ resource_type | upper }} {{ full_name }} \n
{%- if password %} PASSWORD = {{ password | sql }} \n{% endif %}
{%- if login_name %} LOGIN_NAME = {{ login_name | sql }} \n{% endif %}
{%- if display_name %} DISPLAY_NAME = {{ display_name | sql }} \n{% endif %}
{%- if first_name %} FIRST_NAME = {{ first_name | sql }} \n{% endif %}
{%- if middle_name %} MIDDLE_NAME = {{ middle_name | sql }} \n{% endif %}
{%- if last_name %} LAST_NAME = {{ last_name | sql }} \n{% endif %}
{%- if email %} EMAIL = {{  email | sql }} \n{% endif %} 
{%- if must_change_password %} MUST_CHANGE_PASSWORD = TRUE \n{% else %} MUST_CHANGE_PASSWORD = FALSE \n{% endif %}      
{%- if disabled %} DISABLED = TRUE \n{% else %} DISABLED = FALSE \n{% endif %}       
{%- if days_to_expiry %} DAYS_TO_EXPIRY = {{ days_to_expiry | sql }} \n{% endif %}    
{%- if mins_to_unlock %} MINS_TO_UNLOCK = {{ mins_to_unlock | sql }} \n{% endif %} 
{%- if default_warehouse %} DEFAULT_WAREHOUSE = {{ default_warehouse | sql }} \n{% endif %} 
{%- if default_namespace %} DEFAULT_NAMESPACE = {{ default_namespace | sql }} \n{% endif %} 
{%- if default_role %} DEFAULT_ROLE = {{ default_role }} \n{% endif %} 
{%- if mins_to_bypass_mfa %} MINS_TO_BYPASS_MFA = {{ mins_to_bypass_mfa | sql }} \n{% endif %}  
{%- if rsa_public_key  %} RSA_PUBLIC_KEY = {{ rsa_public_key | sql }} \n{% endif %} 
{%- if rsa_public_key_2  %} RSA_PUBLIC_KEY_2 = {{ rsa_public_key_2 | sql }} \n{% endif %} 
{%- if network_policy  %} NETWORK_POLICY = {{ network_policy | sql }} \n{% endif %} 
{%- if comment %} COMMENT = {{ comment | sql }} {% endif %}
""")

        sql.append(template.render({
            **inputs,
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type,
        }))
        print(f"inputs={inputs}")
        for grant in inputs["grant_roles"]:
            sql.append(
                f"GRANT ROLE {grant} TO USER {self._get_full_object_name(inputs, name)}")

        return sql

    def generate_sql_drop_statement(self, name, inputs, environment):
        template = environment.from_string(
            "DROP {{ resource_type | upper }} {{ full_name }}")
        sql = template.render({
            "full_name": self._get_full_object_name(inputs, name),
            "resource_type": self.resource_type
        })
        return sql

    def _get_full_object_name(self, inputs, name):
        return name
