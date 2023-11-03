import unittest
from src.day04 import HashFinder


class TestDay04(unittest.TestCase):
    def test_find_lowest_number_with_valid_hash_abcdef(self):
        hash_finder = HashFinder("abcdef", "00000")
        self.assertEqual(hash_finder.find_lowest_number_with_valid_hash(), 609043)

    def test_find_lowest_number_with_valid_hash_pqrstuv(self):
        hash_finder = HashFinder("pqrstuv", "00000")
        self.assertEqual(hash_finder.find_lowest_number_with_valid_hash(), 1048970)


if __name__ == "__main__":
    unittest.main()
