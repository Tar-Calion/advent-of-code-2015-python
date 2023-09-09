import pytest
from src.day03 import visit_houses_and_count, visit_houses_with_robot_santa_and_count


def test_visit_houses_and_count():
    # Empty input
    assert visit_houses_and_count("") == 1

    # Single move
    assert visit_houses_and_count(">") == 2

    # Multiple moves in same direction
    assert visit_houses_and_count(">>>") == 4

    # Multiple moves in different directions
    assert visit_houses_and_count("^>v<") == 4

    # Multiple moves with backtracking
    assert visit_houses_and_count("^v^v^v^v^v") == 2

    # Negative coordinates
    assert visit_houses_and_count("vvvv") == 5


def test_visit_houses_with_robot_santa_and_count():
    # Empty input
    assert visit_houses_with_robot_santa_and_count("") == 1

    # Single move of santa
    assert visit_houses_with_robot_santa_and_count(">") == 2

    # Single move of robot santa
    assert visit_houses_with_robot_santa_and_count(">^") == 3

    # Multiple moves of santa and robot santa
    assert visit_houses_with_robot_santa_and_count("^>v<") == 3

    # Multiple moves of santa and robot santa with backtracking
    assert visit_houses_with_robot_santa_and_count("^v^v^v^v^v") == 11

    # Negative coordinates
    assert visit_houses_with_robot_santa_and_count("vvvv") == 3
