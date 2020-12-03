import pytest

from advent_of_code.y2020.day3 import *


def test_day_1b():
    with open('./tests/y2020/day3/test_input.txt') as f:
        ski_map = [line.rstrip() for line in f.readlines()]

    assert tree_product(ski_map) == 336
