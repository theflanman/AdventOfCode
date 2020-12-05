import pytest

from advent_of_code.y2020.day3 import *


def test_day_3a():
    with open('./tests/y2020/day3/test_input.txt') as f:
        ski_map = [line.rstrip() for line in f.readlines()]

    assert find_trees(ski_map) == 7
