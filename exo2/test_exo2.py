import unittest

from exo2 import Strings


class Exo1Test(unittest.TestCase):

    def test_item_construction(self):

        fixed_tests_False = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs")
        ]
        fixed_tests_True = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails")
        ]

        fixed_tests_True=Strings(fixed_tests_True)
        self.assertEqual(True, fixed_tests_True.True_or_False)

        fixed_tests_False=Strings(fixed_tests_False)
        self.assertEqual(True, fixed_tests_False.True_or_False)
