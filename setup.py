import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pulumi_snowflake",
    version="0.0.1",
    #description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=[ 'pulumi_snowflake' ],
    python_requires='>=3.6',
    install_requires=[
        'pulumi>=1.0.0',
        'snowflake-connector-python>=2.1.3'
    ]
)