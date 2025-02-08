import unittest
from src.day08 import count_string_literals, calculate_memory_characters

class TestDay08(unittest.TestCase):
    def test_count_string_literals_parameterized(self):
        test_cases = [
            ('""\n"abc"\n"a\\\\aa\\"aaa"\n"\\x27"', 13),
            ('""', 2),
            ('"azlgxdbljwygyttzkfwuxv"', 2),
            ('"aaa\\"aaa"', 3),
            ('"d\\\\gkbqo\\\\fwukyxabu"', 4),
            ('"\\x27"', 5),
        ]
        for input_string, expected in test_cases:
            with self.subTest(input_string=input_string):
                result = count_string_literals(input_string)
                self.assertEqual(result, expected)

    def test_calculate_memory_characters_parameterized(self):
        test_cases = [
            ('""', 0),
            ('"abc"', 3),
            ('"aaa\\"aaa"', 7),
            ('"d\\\\gkbqo\\\\fwukyxabu"', 17),
            ('"\\x27"', 1),
        ]
        for input_string, expected in test_cases:
            with self.subTest(input_string=input_string):
                result = calculate_memory_characters(input_string)
                self.assertEqual(result, expected)

