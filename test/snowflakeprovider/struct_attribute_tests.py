import unittest

from pulumi_snowflake.snowflakeprovider import StringAttribute, BooleanAttribute
from pulumi_snowflake.snowflakeprovider.struct_attribute import StructAttribute

class TestStructObject:

    def __init__(self, field1: str, field2: bool, field3: str = None):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


class StructAttributeTests(unittest.TestCase):

    def test_generate_sql(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
        ])

        sql = attr.generate_sql(TestStructObject('field1value', True))

        self.assertEqual(sql, "TESTATTR = (FIELD1 = %s, FIELD2 = TRUE)")

    def test_when_generate_sql_and_value_does_not_have_field_then_exception(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2not_exist', True),
        ])

        self.assertRaises(Exception, attr.generate_sql, TestStructObject('field1value', True))

    def test_generate_bindings(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        bindings = attr.generate_bindings(TestStructObject('field1value', True, 'field3value'))

        self.assertEqual(bindings, ('field1value','field3value'))


    def test_generate_outputs(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        output = attr.generate_outputs(TestStructObject('field1value', True, 'field3value'))

        self.assertEqual(output, {
            'field1': 'field1value',
            'field2': True,
            'field3': 'field3value'
        })
