import unittest

from pulumi_snowflake import NoneToken
from pulumi_snowflake.provider import StringAttribute
from pulumi_snowflake.provider import ValueOrNoneAttribute


class ValueOrNoneTests(unittest.TestCase):

    def test_when_given_attribute_then_inherits_parameters(self):

        attr = ValueOrNoneAttribute(StringAttribute("myfield", True))

        self.assertEqual(attr.name, "myfield")
        self.assertEqual(attr.required, True)

    def test_when_value_is_none_generate_sql_is_correct(self):
        attr = ValueOrNoneAttribute(StringAttribute("myfield", True))
        sql = attr.generate_sql(NoneToken().as_dict())
        self.assertEqual(sql, "MYFIELD = NONE")

    def test_when_value_is_none_bindings_are_correct(self):
        attr = ValueOrNoneAttribute(StringAttribute("myfield", True))
        bindings = attr.generate_bindings(NoneToken().as_dict())
        self.assertEqual(bindings, None)

    def test_when_value_is_str_generate_sql_is_correct(self):
        attr = ValueOrNoneAttribute(StringAttribute("myfield", True))
        sql = attr.generate_sql("astring")
        self.assertEqual(sql, "MYFIELD = %s")

    def test_when_value_is_str_bindings_are_correct(self):
        attr = ValueOrNoneAttribute(StringAttribute("myfield", True))
        bindings = attr.generate_bindings("astring")
        self.assertEqual(bindings, ("astring",))
