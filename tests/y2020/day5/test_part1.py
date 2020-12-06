import pytest

from advent_of_code.y2020.day5 import *


@pytest.mark.parametrize('seat_str, expected',
                         [('BFFFBBFRRR', 567),
                          ('FFFBBBFRRR', 119),
                          ('BBFFBBFRLL', 820),
                          ])
def test_day_5a_parse_id(seat_str, expected):
    assert parse_seat(seat_str) == expected
