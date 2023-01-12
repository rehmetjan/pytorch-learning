import numpy as np


def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    # ys = [1.7 * x + np.random.rand() / 5 for x in xs]
    ys = [1.2 * x + np.random.rand() / 10 for x in xs]
    # ys = np.random.rand(counts)
    return xs, ys
