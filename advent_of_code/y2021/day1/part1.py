import numpy as np
import scipy.signal

from advent_of_code.y2021.day1 import preprocess


def ascending(vals):
    return (np.diff(vals) > 0).sum()


def windowed_ascending(vals):
    return ascending(scipy.signal.convolve(vals, [1]*3, 'valid'))


if __name__ == '__main__':
    with open('./advent_of_code/y2021/day1/input.txt') as f:
        input_data = f.read()

    data = preprocess(input_data)

    print(ascending(data))

    print(windowed_ascending(data))
