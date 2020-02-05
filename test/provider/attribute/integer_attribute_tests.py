import unittest

from pulumi_snowflake.provider.attribute import IntegerAttribute


class IntegerAttributeTests(unittest.TestCase):

    def test_generate_sql(self):
        attr = IntegerAttribute("myint", True)
        sql = attr.generate_sql(1234)
        self.assertEqual(sql, "MYINT = 1234")

    def test_bindings(self):
        attr = IntegerAttribute("myint", True)
        bindings = attr.generate_bindings(1234)
        self.assertEqual(bindings, None)

    def test_when_value_not_number_then_generate_sql_throws_exception(self):
        attr = IntegerAttribute("myint", True)
        self.assertRaises(Exception, attr.generate_sql, "123d")

    def test_when_value_not_number_then_generate_bindings_throws_exception(self):
        attr = IntegerAttribute("myint", True)
        self.assertRaises(Exception, attr.generate_bindings, "123d")
