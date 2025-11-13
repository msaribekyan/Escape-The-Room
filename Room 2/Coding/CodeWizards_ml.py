# Write a function that calculates the cosine similarity between two NumPy vectors.

import numpy as np
from numpy.linalg import norm

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray):
    
    if vec1.ndim != 1 or vec1.shape != vec2.shape:
       return 0

    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))
