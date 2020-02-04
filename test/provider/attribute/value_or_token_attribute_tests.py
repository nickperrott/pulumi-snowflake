import unittest

from pulumi_snowflake.provider import StringAttribute
from pulumi_snowflake.provider.attribute.value_or_token_attribute import ValueOrTokenAttribute
from pulumi_snowflake.token import Token


class ValueOrTokenTests(unittest.TestCase):

    def test_when_given_attribute_then_inherits_parameters(self):
        attr = ValueOrTokenAttribute(StringAttribute("myfield", True), Token("TOKEN"))
        self.assertEqual(attr.name, "myfield")
        self.assertEqual(attr.required, True)

    def test_when_value_is_token_generate_sql_is_correct(self):
        attr = ValueOrTokenAttribute(StringAttribute("myfield", True), Token("TOKEN"))
        sql = attr.generate_sql(Token("TOKEN"))
        self.assertEqual(sql, "MYFIELD = TOKEN")

    def test_when_value_is_token_bindings_are_correct(self):
        attr = ValueOrTokenAttribute(StringAttribute("myfield", True), Token("TOKEN"))
        bindings = attr.generate_bindings(Token("TOKEN"))
        self.assertEqual(bindings, None)

    def test_when_value_is_str_generate_sql_is_correct(self):
        attr = ValueOrTokenAttribute(StringAttribute("myfield", True), Token("TOKEN"))
        sql = attr.generate_sql("astring")
        self.assertEqual(sql, "MYFIELD = %s")

    def test_when_value_is_str_bindings_are_correct(self):
        attr = ValueOrTokenAttribute(StringAttribute("myfield", True), Token("TOKEN"))
        bindings = attr.generate_bindings("astring")
        self.assertEqual(bindings, ("astring",))
