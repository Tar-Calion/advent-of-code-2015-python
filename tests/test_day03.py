import pytest
from src.day03 import visit_houses


def test_visit_houses():
    # Empty input
    assert len(visit_houses("")) == 1

    # Single move
    assert len(visit_houses(">")) == 2

    # Multiple moves in same direction
    assert len(visit_houses(">>>")) == 4

    # Multiple moves in different directions
    assert len(visit_houses("^>v<")) == 4

    # Multiple moves with backtracking
    assert len(visit_houses("^v^v^v^v^v")) == 2

    # Negative coordinates
    assert len(visit_houses("vvvv")) == 5
