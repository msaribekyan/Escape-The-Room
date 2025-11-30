# Write a function that calculates the Euclidean distance between two NumPy vectors.

import numpy as np
from numpy.linalg import norm

def euclidean_distance(vec1: np.ndarray, vec2: np.ndarray):

    try:
        return norm(vec2 - vec1)
    except:
        return 0
