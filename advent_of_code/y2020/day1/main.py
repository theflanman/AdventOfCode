def part1(data):
    for i in range(len(data)):
        if data[i] > 2020:
            continue
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i]*data[j]


def part2(data):
    for i in range(len(data)):
        if data[i] > 2020:
            continue
        for j in range(i + 1, len(data)):
            if data[i] + data[j] >= 2020:
                continue
            else:
                for k in range(j + 1, len(data)):
                    if data[i] + data[j] + data[k] == 2020:
                        return data[i]*data[j]*data[k]


if __name__ == '__main__':
    with open('./advent_of_code/y2020/day1/input.txt') as f:
        input_data = [int(l) for l in f.readlines()]

    print(f'Part 1: {part1(input_data)}')

    print(f'Part 2: {part2(input_data)}')
