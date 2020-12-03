import re


def parse_policy(pass_code):
    pattern = r'(\d+)-(\d+) ([a-zA-Z]): (.*)'
    return re.match(pattern, pass_code).groups()


def pass_valid_1(low, high, key, password):
    key_count = password.count(key)
    if key_count < int(low) or key_count > int(high):
        return False
    else:
        return True


def pass_valid_2(first, second, key, password):
    return (password[int(first)-1] == key) ^ (password[int(second)-1] == key)


def part1(data):
    return sum([pass_valid_1(*pass_code) for pass_code in data])


def part2(data):
    return sum([pass_valid_2(*pass_code) for pass_code in data])


if __name__ == '__main__':
    with open('./advent_of_code/y2020/day2/input.txt') as f:
        input_data = [parse_policy(l) for l in f.readlines() if l is not None]

    print(f'Part 1: {part1(input_data)}')

    print(f'Part 2: {part2(input_data)}')
