import numpy as np


def conjugate(q):
    return np.array([-x for x in q[:-1]] + [q[-1]])
