# pulumi-snowflake AWS Example

This folder contains an example Pulumi program which creates a set of Snowflake resources.

> **NOTE:** Pulumi has some problems with Dynamic Providers in Python on Windows and may not work on this platform.  [See this GitHub issue](https://github.com/pulumi/pulumi/issues/3807).

To run this example:

* Install and start a VirtualEnv in this folder
* Locally install (or reinstall) the `pulumi-snowflake` package from the root directory:

```
pip install -e ..
```

* Set your Snowflake credentials:

```
pulumi config set snowflakeAccountName [snowflake account name]
pulumi config set --secret snowflakeUsername [snowflake username]
pulumi config set --secret snowflakePassword [snowflake password]
pulumi config set --secret snowflakeRole [desired role]
```

> Note that `snowflakeRole` is optional, however your role must have adequate privilages to create storage integrations to run this example.  By default, the `SYSADMIN` role does not have these privilages, but `ACCOUNTADMIN` does.

* Create a database named "MyDatabase2" and schema named "MySchema2", or comment out the "Explicit Provider" example in
`__main__.py`
* Deploy the stack:

```
pulumi up
```
