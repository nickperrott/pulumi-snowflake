import unittest

from jinja2 import Template


class JinjaTemplateTests(unittest.TestCase):

    # TODO: move these macros to a shared location so they can be used by all resources

    macros = """
{%- macro str_to_sql(v) -%}
    '{{ v }}'
{%- endmacro -%}

{%- macro num_to_sql(v) -%}
    {%- if v | int == v -%}
        {{ v | int }}
    {%- else -%}
        {{ v }}
    {%- endif -%}
{%- endmacro -%}

{%- macro list_to_sql(l) -%}
    ({% for item in l -%}
        {{ to_sql(item) }}{{ "," if not loop.last }}
    {%- endfor -%})
{%- endmacro -%}

{%- macro dict_to_sql(d) -%}
    ({% for key in d.keys() -%}
        {{ key | upper }} = {{ to_sql(d[key]) }}{{ "," if not loop.last }}
    {%- endfor -%})
{%- endmacro -%}

{%- macro to_sql(v) -%}
    {%- if v is string -%}
        {{ str_to_sql(v) }}
    {%- elif v is integer -%}
        {{ num_to_sql(v) }}
    {%- elif v is float -%}
        {{ num_to_sql(v) }}
    {%- elif v is mapping -%}
        {{ dict_to_sql(v) }}
    {%- elif v is sequence -%}
        {{ list_to_sql(v) }}
    {%- endif -%}
{%- endmacro -%}


"""

    def test_when_str_converted_to_sql_then_is_correct_syntax(self):
        template = Template(self.macros + "{{ to_sql(test_str) }}")

        sql = template.render({
            "test_str": "my_string"
        })

        self.assertEqual(sql, "'my_string'")

    def test_when_int_converted_to_sql_then_is_correct_syntax(self):
        template = Template(self.macros + "{{ to_sql(test_int) }}")

        sql = template.render({
            "test_int": 123
        })

        self.assertEqual(sql, "123")

    def test_when_float_converted_to_sql_then_is_correct_syntax(self):
        template = Template(self.macros + "{{ to_sql(test_float) }}")

        sql = template.render({
            "test_float": 123.456
        })

        self.assertEqual(sql, "123.456")

    def test_when_whole_numbered_float_converted_to_sql_then_generates_int(self):
        template = Template(self.macros + "{{ to_sql(test_float) }}")

        sql = template.render({
            "test_float": 123.0
        })

        self.assertEqual(sql, "123")

    def test_when_list_converted_to_sql_then_is_correct_syntax(self):
        template = Template(self.macros + "{{ to_sql(test_list) }}")

        sql = template.render({
            "test_list": [ "item1", "item2" ]
        })

        self.assertEqual(sql, "('item1','item2')")

    def test_when_dict_converted_to_sql_then_is_correct_syntax(self):
        template = Template(self.macros + "{{ to_sql(test_dict) }}")

        sql = template.render({
            "test_dict": {
                "item1": "val1",
                "item2": "val2"
            }
        })

        self.assertEqual(sql, "(ITEM1 = 'val1',ITEM2 = 'val2')")

    def test_when_dict_converted_to_sql_then_handles_any_value_type(self):
        template = Template(self.macros + "{{ to_sql(test_dict) }}")

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