import unittest

from pulumi_snowflake import AutoToken
from pulumi_snowflake.provider import StringAttribute
from pulumi_snowflake.provider.attribute.value_or_auto_attribute import ValueOrAutoAttribute


class ValueOrAutoTests(unittest.TestCase):

    def test_when_given_attribute_then_inherits_parameters(self):

        attr = ValueOrAutoAttribute(StringAttribute("myfield", True))

        self.assertEqual(attr.name, "myfield")
        self.assertEqual(attr.required, True)

    def test_when_value_is_auto_generate_sql_is_correct(self):
        attr = ValueOrAutoAttribute(StringAttribute("myfield", True))
        sql = attr.generate_sql(AutoToken())
        self.assertEqual(sql, "MYFIELD = AUTO")

    def test_when_value_is_auto_bindings_are_correct(self):
        attr = ValueOrAutoAttribute(StringAttribute("myfield", True))
        bindings = attr.generate_bindings(AutoToken())
        self.assertEqual(bindings, None)

    def test_when_value_is_str_generate_sql_is_correct(self):
        attr = ValueOrAutoAttribute(StringAttribute("myfield", True))
        sql = attr.generate_sql("astring")
        self.assertEqual(sql, "MYFIELD = %s")

    def test_when_value_is_str_bindings_are_correct(self):
        attr = ValueOrAutoAttribute(StringAttribute("myfield", True))
        bindings = attr.generate_bindings("astring")
        self.assertEqual(bindings, ("astring",))
