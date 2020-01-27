import unittest

from pulumi_snowflake.random_id import RandomId


class RandomIdTests(unittest.TestCase):

    def test_when_char_is_1_then_matches(self):
        self.assertRegex(RandomId.generate(1), '^[a-f,0-9]$')

    def test_when_char_is_2_then_matches(self):
        self.assertRegex(RandomId.generate(2), '^[a-f,0-9]{2}$')

    def test_when_char_is_3_then_matches(self):
        self.assertRegex(RandomId.generate(3), '^[a-f,0-9]{3}$')

    def test_when_char_is_7_then_matches(self):
        self.assertRegex(RandomId.generate(7), '^[a-f,0-9]{7}$')
