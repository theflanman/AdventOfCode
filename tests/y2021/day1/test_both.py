import pytest

from advent_of_code.y2021.day1 import preprocess
from advent_of_code.y2021.day1.part1 import ascending, windowed_ascending

test_input = \
    """199
    200
    208
    210
    200
    207
    240
    269
    260
    263"""


def test_part1():
    test_data = preprocess(test_input)

    assert ascending(test_data) == 7


def test_part2():
    test_data = preprocess(test_input)

    assert windowed_ascending(test_data) == 5
