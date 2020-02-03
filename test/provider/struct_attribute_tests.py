import unittest

from pulumi_snowflake.provider import StringAttribute, BooleanAttribute, StructAttribute

class StructAttributeTests(unittest.TestCase):

    def test_generate_sql(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
        ])

        sql = attr.generate_sql({
            'field1': 'field1value',
            'field2': True
        })

        self.assertEqual(sql, "TESTATTR = (FIELD1 = %s, FIELD2 = TRUE)")

    def test_when_generate_sql_and_value_does_not_have_field_then_exception(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2not_exist', True),
        ])

        self.assertRaises(Exception, attr.generate_sql, {
            'field1': 'field1value',
            'field2': True
        })

    def test_generate_bindings(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        bindings = attr.generate_bindings({
            'field1': 'field1value',
            'field2': True,
            'field3': 'field3value'
        })

        self.assertEqual(bindings, ('field1value','field3value'))


    def test_generate_outputs(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        output = attr.generate_outputs({
            'field1': 'field1value',
            'field2': True,
            'field3': 'field3value'
        })

        self.assertEqual(output, {
            'field1': 'field1value',
            'field2': True,
            'field3': 'field3value'
        })

    def test_when_required_field_is_none_then_exception(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
        ])

        self.assertRaises(Exception, attr.generate_sql, {
            'field1': None,
            'field2': True
        })

    def test_when_field_is_none_then_not_in_sql(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', False),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        sql = attr.generate_sql({
            'field1': None,
            'field2': True,
            'field3': 'field3value'
        })

        self.assertEqual(sql, "TESTATTR = (FIELD2 = TRUE, FIELD3 = %s)")

    def test_when_required_field_is_not_present_then_exception(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', True),
            BooleanAttribute('field2', True),
        ])

        self.assertRaises(Exception, attr.generate_sql, {
            'field2': True
        })

    def test_when_field_is_not_present_then_not_in_sql(self):

        attr = StructAttribute('TestAttr', True, [
            StringAttribute('field1', False),
            BooleanAttribute('field2', True),
            StringAttribute('field3', True)
        ])

        sql = attr.generate_sql({
            'field2': True,
            'field3': 'field3value'
        })

        self.assertEqual(sql, "TESTATTR = (FIELD2 = TRUE, FIELD3 = %s)")
