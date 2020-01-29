# pulumi-snowflake AWS Example

This folder contains an example Pulumi program which creates a Snowflake file format.

> **NOTE:** Pulumi has some problems with Dynamic Providers in Python on Windows and may not work on this platform.  [See this GitHub issue](https://github.com/pulumi/pulumi/issues/3807).

To run this example:

* Install and start a VirtualEnv in this folder
* Locally install (or reinstall) the `pulumi-snowflake` package from the root directory:

```
pip install -e ..
```

* Set your Snowflake credentials:

```
pulumi config set snowflakeAccountName [your Snowflake account name]
pulumi config set --secret snowflakeUsername [your Snowflake username]
pulumi config set --secret snowflakePassword [snowflake password]
```

* Set your Snowflake table and schema name in `__main__.py`.
* Deploy the stack:

```
pulumi up
```
