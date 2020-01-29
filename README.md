# pulumi-snowflake

This project contains a pip packaged named `pulumi-snowflake` which allows Snowflake resources to be managed in Pulumi.

> **NOTE:** This package relies on the `snowflake-connector-python` pip package, which has specific setup instructions.  [Please ensure you check the prerequesits for your platform](https://docs.snowflake.net/manuals/user-guide/python-connector-install.html) before using the `pulumi-snowflake` package.

An example Pulumi program which uses this package is present in the `example` folder.

## Prerequesits

* Install the package into your Pulumi project using `pip`
* Set your Snowflake credentials in your stack config:

```
pulumi config set snowflakeAccountName [snowflake account name]
pulumi config set --secret snowflakeUsername [snowflake username]
pulumi config set --secret snowflakePassword [snowflake password]
```

## Resources

Currently this package supports a single resource.

* The `pulumi_snowflake.FileFormat` class is a Pulumi resource for managing [Snowflake file format objects](https://docs.snowflake.net/manuals/sql-reference/sql/create-file-format.html).


## Development

* To run the unit tests (you may also want to instantiate a virtual environment in the root directory):

```
python setup.py test
```
