import pytest

from advent_of_code.y2020.day1 import *


def test_day_1b():
    input_data = [1721, 979, 366, 299, 675, 1456]
    assert part2(input_data) == 241861950
