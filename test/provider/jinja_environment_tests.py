import unittest

from jinja2.environment import Environment

from pulumi_snowflake.baseprovider.filters import to_sql, to_identifier


class JinjaEnvironmentTests(unittest.TestCase):

    def test_when_str_converted_to_sql_then_is_correct_syntax(self):
        template = self.get_environment().from_string("{{ test_str | sql }}")

        sql = template.render({
            "test_str": "my_string"
        })

        self.assertEqual(sql, "'my_string'")

    def test_when_int_converted_to_sql_then_is_correct_syntax(self):
        template = self.get_environment().from_string("{{ test_int | sql }}")

        sql = template.render({
            "test_int": 123
        })

        self.assertEqual(sql, "123")

    def test_when_float_converted_to_sql_then_is_correct_syntax(self):
        template = self.get_environment().from_string("{{ test_float | sql }}")

        sql = template.render({
            "test_float": 123.456
        })

        self.assertEqual(sql, "123.456")

    def test_when_whole_numbered_float_converted_to_sql_then_generates_int(self):
        template = self.get_environment().from_string("{{ test_float | sql }}")

        sql = template.render({
            "test_float": 123.0
        })

        self.assertEqual(sql, "123")

    def test_when_list_converted_to_sql_then_is_correct_syntax(self):
        template = self.get_environment().from_string("{{ test_list | sql }}")

        sql = template.render({
            "test_list": [ "item1", "item2" ]
        })

        self.assertEqual(sql, "('item1','item2')")

    def test_when_dict_converted_to_sql_then_is_correct_syntax(self):
        template = self.get_environment().from_string("{{ test_dict | sql }}")

        sql = template.render({
            "test_dict": {
                "item1": "val1",
                "item2": "val2"
            }
        })

        self.assertEqual(sql, "(ITEM1 = 'val1',ITEM2 = 'val2')")

    def test_when_dict_converted_to_sql_then_handles_any_value_type(self):
        template = self.get_environment().from_string("{{ test_dict | sql }}")

        sql = template.render({
            "test_dict": {
                "item1": "val1",
                "item2": {
                    "sub1": "v2"
                },
                "item3": ["l1", "l2"],
                "item4": 45.0,
            }
        })

        self.assertEqual(sql, "(ITEM1 = 'val1',ITEM2 = (SUB1 = 'v2'),ITEM3 = ('l1','l2'),ITEM4 = 45)")


    # HELPERS

    def get_environment(self):
        environment = Environment()
        environment.filters["sql"] = to_sql
        environment.filters["sql_identifier"] = to_identifier
        return environment