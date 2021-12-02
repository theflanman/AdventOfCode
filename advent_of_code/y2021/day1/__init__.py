import numpy as np


def preprocess(input_str: str):
    return np.array([int(line) for line in input_str.splitlines()])
