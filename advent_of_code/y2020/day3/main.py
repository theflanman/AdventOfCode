def find_trees(tree_map, run=3, fall=1):
    pos = 0
    trees = 0
    width = len(tree_map[0])
    for line in tree_map[::fall]:
        if line[pos] == '#':
            trees += 1
        #     line = line[:pos] + 'X' + line[pos+1:]
        # else:
        #     line = line[:pos] + 'O' + line[pos+1:]
        # print(line)
        pos = (pos + run) % width

    return trees


def tree_product(ski_map):
    product = 1
    for fall, run in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        product *= find_trees(ski_map, run=run, fall=fall)
    return product


if __name__ == '__main__':
    with open('./advent_of_code/y2020/day3/input.txt') as f:
        ski_map = [line.rstrip() for line in f.readlines()]

    print(f'part 1: {find_trees(ski_map)}')

    print(f'part 2: {tree_product(ski_map)}')
