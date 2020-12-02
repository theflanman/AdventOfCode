import pytest

from advent_of_code.y2020.day1 import *


def test_day_1a():
    input_data = [1721, 979, 366, 299, 675, 1456]
    assert part1(input_data) == 514579
