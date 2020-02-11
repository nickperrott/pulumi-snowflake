import unittest

from pulumi_snowflake.baseprovider.attribute import KeyValueAttribute


class KeyValueAttributeTests(unittest.TestCase):

    def test_when_value_is_string_then_generates_sql_string(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings("test_string")
        self.assertEqual(sql, "TEST_ATTR = %s")
        self.assertEqual(bindings, ("test_string",))

    def test_when_value_is_string_then_generates_sql_int(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(1234)
        self.assertEqual(sql, "TEST_ATTR = 1234")
        self.assertEqual(bindings, tuple())

    def test_when_value_is_float_then_generates_sql_float(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(1234.5)
        self.assertEqual(sql, "TEST_ATTR = 1234.5")
        self.assertEqual(bindings, tuple())

    def test_when_value_is_integer_float_then_generates_sql_int(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(1234.0)
        self.assertEqual(sql, "TEST_ATTR = 1234")
        self.assertEqual(bindings, tuple())

    def test_when_value_is_bool_true_then_generates_sql_bool(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(True)
        self.assertEqual(sql, "TEST_ATTR = TRUE")
        self.assertEqual(bindings, tuple())

    def test_when_value_is_bool_false_then_generates_sql_bool(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(False)
        self.assertEqual(sql, "TEST_ATTR = FALSE")
        self.assertEqual(bindings, tuple())

    def test_when_value_is_dict__then_generates_sql_object(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings({
            "field1": "val1",
            "field2": 123,
            "field3": "val2",
        })
        self.assertEqual(sql, "TEST_ATTR = (FIELD1 = %s, FIELD2 = 123, FIELD3 = %s)")
        self.assertEqual(bindings, ("val1","val2"))

    def test_when_value_is_list_then_generates_sql_list(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(["val1", 1234, "val2"])
        self.assertEqual(sql, "TEST_ATTR = (%s,1234,%s)")
        self.assertEqual(bindings, ("val1","val2"))

    def test_when_value_is_object_then_throws_exception(self):
        class TestClass:
            pass

        attr = KeyValueAttribute("test_attr")
        self.assertRaises(Exception, attr.generate_sql_and_bindings, TestClass())

    def test_when_value_is_none_then_generates_empty_string(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings(None)
        self.assertEqual(sql, "")
        self.assertEqual(bindings, tuple())

    def test_when_dict_contains_none_then_field_not_present(self):
        attr = KeyValueAttribute("test_attr")
        (sql,bindings) = attr.generate_sql_and_bindings({
            "field1": None,
            "field2": "111"
        })
        self.assertEqual(sql, "TEST_ATTR = (FIELD2 = %s)")
        self.assertEqual(bindings, ("111",))
