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
pulumi config set --secret snowflakeRole [snowflake role]
```

> Note: `snowflakeRole` is optional.

## Resources

Currently this package supports a the following resources:

* The `pulumi_snowflake.fileformat.FileFormat` class is a Pulumi resource for managing [Snowflake file format objects](https://docs.snowflake.net/manuals/sql-reference/sql/create-file-format.html).
* The `pulumi_snowflake.storage_integration.AWSStorageIntegration` class is a Pulumi resource for managing [storage integration objects with AWS parameters](https://docs.snowflake.net/manuals/sql-reference/sql/create-storage-integration.html).
* The `pulumi_snowflake.stage.Stage` class is a Pulumi resource for managing [Snowflake staging areas](https://docs.snowflake.net/manuals/sql-reference/sql/create-stage.html)
* The `pulumi_snowflake.database.Database` class is a Pulumi resource for managing [Snowflake databases](https://docs.snowflake.net/manuals/sql-reference/sql/create-database.html)
* The `pulumi_snowflake.schema.Schema` class is a Pulumi resource for managing [Snowflake schemas](https://docs.snowflake.net/manuals/sql-reference/sql/create-schema.html)

## Development

The directory structure is as follows:

```
├── example                     # An example of a Pulumi program using this package with AWS
├── pulumi_snowflake            # The main package source
│   ├── baseprovider            # The dynamic provider base class and related classes
│   │   └── attribute
│   ├── database                # The Database resource and dynamic provider
│   ├── fileformat              # The File Format resource and dynamic provider
│   ├── schema                  # The Schema resource and dynamic provider
│   ├── stage                   # The Stage resource and dynamic provider
│   └── storageintegration      # The Storage Integration resource and dynamic provider
└── test                        # Unit tests
    ├── fileformat
    ├── provider
    │   └── attribute
    ├── stage
    └── storageintegration
```

### Unit tests

* To run the unit tests (you may also want to instantiate a virtual environment in the root directory):

```
python setup.py test
```

### Generic object provider framework

The dynamic providers for each object type are build on top of some generic classes which make it straightforward to support new object types in the future.  The `BaseDynamicProvider` class handles the `create`, `diff` and `delete` methods based on a few parameters which define the Snowflake object.  These objects take a `Provider` parameters object, a Snowflake connection, the object name, and a list of attributes in their constructor.  For example, the file format object provider is defined like so:

```python
class FileFormatProvider(Provider):
    def __init__(self, provider: Provider, connection_provider: ConnectionProvider):
        super().__init__(connection_provider, "FILE FORMAT", [
            KeyValueAttribute("type"),
            KeyValueAttribute("comment")
        ])
```

Notice how the attributes list is used to define the structure of `CREATE` and `UPDATE` calls to the object in a manner that [matches the documentation](https://docs.snowflake.net/manuals/sql-reference/sql/create-file-format.html).  The values in the attribute list are all subclasses of `BaseAttribute`, which define properties of the attributes and the way they are turned into SQL fragments.
