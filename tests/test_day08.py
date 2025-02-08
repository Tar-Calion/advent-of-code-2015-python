import unittest
from src.day08 import count_string_literals, calculate_memory_characters

class TestDay08(unittest.TestCase):
    def test_count_string_literals_with_newlines(self):
        input_string = '""\n"abc"\n"a\\\\aa\\"aaa"\n"\\x27"'
        result = count_string_literals(input_string)
        self.assertEqual(result, 13)  # Expected result based on the example input

    def test_empty_string(self):
        input_string = '""'
        result = count_string_literals(input_string)
        self.assertEqual(result, 2)  # 2 - 0 = 2

    def test_simple_string(self):
        input_string = '"azlgxdbljwygyttzkfwuxv"'
        result = count_string_literals(input_string)
        self.assertEqual(result, 2)  # 26 - 24 = 2

    def test_escaped_quotes(self):
        input_string = '"aaa\\"aaa"'
        result = count_string_literals(input_string)
        self.assertEqual(result, 3)  # 10 - 7 = 3

    def test_escaped_backslashes(self):
        input_string = '"d\\\\gkbqo\\\\fwukyxabu"'
        result = count_string_literals(input_string)
        self.assertEqual(result, 4)  # 20 - 16 = 4

    def test_hexadecimal_escapes(self):
        input_string = '"\\x27"'
        result = count_string_literals(input_string)
        self.assertEqual(result, 5)  # 6 - 1 = 5

    def test_calculate_memory_characters(self):
        self.assertEqual(calculate_memory_characters('""'), 0)
        self.assertEqual(calculate_memory_characters('"abc"'), 3)
        self.assertEqual(calculate_memory_characters('"aaa\\"aaa"'), 7)
        self.assertEqual(calculate_memory_characters('"d\\\\gkbqo\\\\fwukyxabu"'), 17)
        self.assertEqual(calculate_memory_characters('"\\x27"'), 1)

if __name__ == "__main__":
    unittest.main()
