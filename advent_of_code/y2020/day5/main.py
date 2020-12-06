def parse_seat(seat_str):
    row = 0
    column = 0

    for r in seat_str[:7]:
        if r == 'B':
            row += 1
        elif r != 'F':
            raise ValueError(f'row indicator {r} is invalid')
        row <<= 1
    row >>= 1

    for c in seat_str[7:]:
       if c == 'R':
           column += 1
       elif c != 'L':
           raise ValueError(f'column indicator {c} is invalid')
       column <<= 1
    column >>= 1

    return row*8 + column


def part1(input_data):
    return max([parse_seat(b_pass) for b_pass in input_data])


def part2(input_data):
    seats_list = sorted([parse_seat(b_pass) for b_pass in input_data])

    first_seat = seats_list[0]
    last_seat = seats_list[-1]

    for i in range(first_seat + 1, last_seat):
        if i not in seats_list:
            return i

    raise EOFError


if __name__ == '__main__':
    with open('./advent_of_code/y2020/day5/input.txt') as f:
        input_data = [x.rstrip() for x in f.readlines()]

    print(f'Part 1: {part1(input_data)}')

    print(f'Part 2: {part2(input_data)}')
