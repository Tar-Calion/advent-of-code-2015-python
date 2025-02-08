import unittest
from src.day03 import visit_houses_and_count, visit_houses_with_robot_santa_and_count

class TestDay03(unittest.TestCase):
    def test_visit_houses_and_count_empty_input(self):
        self.assertEqual(visit_houses_and_count(""), 1)

    def test_visit_houses_and_count_single_move(self):
        self.assertEqual(visit_houses_and_count(">"), 2)

    def test_visit_houses_and_count_multiple_same_direction(self):
        self.assertEqual(visit_houses_and_count(">>>"), 4)

    def test_visit_houses_and_count_multiple_different_directions(self):
        self.assertEqual(visit_houses_and_count("^>v<"), 4)

    def test_visit_houses_and_count_backtracking(self):
        self.assertEqual(visit_houses_and_count("^v^v^v^v^v"), 2)

    def test_visit_houses_and_count_negative_coordinates(self):
        self.assertEqual(visit_houses_and_count("vvvv"), 5)

    def test_visit_houses_with_robot_santa_and_count_empty_input(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count(""), 1)

    def test_visit_houses_with_robot_santa_and_count_single_move_santa(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count(">"), 2)

    def test_visit_houses_with_robot_santa_and_count_single_move_robot_santa(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count(">^"), 3)

    def test_visit_houses_with_robot_santa_and_count_multiple_moves(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count("^>v<"), 3)

    def test_visit_houses_with_robot_santa_and_count_backtracking(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count("^v^v^v^v^v"), 11)

    def test_visit_houses_with_robot_santa_and_count_negative_coordinates(self):
        self.assertEqual(visit_houses_with_robot_santa_and_count("vvvv"), 3)
