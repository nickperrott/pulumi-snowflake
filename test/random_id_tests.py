import unittest

from pulumi_snowflake.random_id import RandomId


class RandomIdTests(unittest.TestCase):

    def testWhenCharIs1ThenMatches(self):
        self.assertRegex(RandomId.generate(1), '^[a-f,0-9]$')

    def testWhenCharIs2ThenMatches(self):
        self.assertRegex(RandomId.generate(2), '^[a-f,0-9]{2}$')

    def testWhenCharIs3ThenMatches(self):
        self.assertRegex(RandomId.generate(3), '^[a-f,0-9]{3}$')

    def testWhenCharIs7ThenMatches(self):
        self.assertRegex(RandomId.generate(7), '^[a-f,0-9]{7}$')
