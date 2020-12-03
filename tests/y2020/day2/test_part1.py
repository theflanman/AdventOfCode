import pytest

from advent_of_code.y2020.day2 import *


def test_day_1a():
    input_data = ['1-3 a: abcde',
                  '1-3 b: cdefg',
                  '2-9 c: ccccccccc']
    assert part1([parse_policy(d) for d in input_data]) == 2
