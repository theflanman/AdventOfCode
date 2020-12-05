import pytest

from advent_of_code.y2020.day4 import *


def test_day_4a():
    with open('./tests/y2020/day4/test_input.txt') as f:
        input_data = f.read()

    assert part1(input_data) == 2
