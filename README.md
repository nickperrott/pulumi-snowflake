# cs-snowflake-dynamic-provider
Nuage Pulumi Dynamic Provider for Snowflake


NOTE: This package relies on the `snowflake-connector-python` pip package.  [Please ensure you check the prerequesits for your platform](https://docs.snowflake.net/manuals/user-guide/python-connector-install.html) before installing `pulumi-snowflake`

* To use this provider, you must set your Snowflake credentials as part of your Pulumi program's config:

```
pulumi config set snowflakeAccountName [your Snowflake account name]
pulumi config set --secret snowflakeUsername [your Snowflake username]
pulumi config set --secret snowflakePassword [snowflake password]
```