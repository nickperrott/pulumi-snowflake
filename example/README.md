# Pulumi Snowflake AWS Example

* Install and start a VirtualEnv (platform dependant)

* Install (or reinstall) the `pulumi-snowflake` package from the directory above:

```
pip install -e ..
```

* Set your Snowflake credentials

```
pulumi config set snowflakeAccountName [your Snowflake account name]
pulumi config set --secret snowflakeUsername [your Snowflake username]
pulumi config set --secret snowflakePassword [snowflake password]
```

* Deploy the stack

```
pulumi up
```
