# Write a function that calculates the cosine similarity between two NumPy vectors.

import numpy as np
from numpy.linalg import norm

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray):
    
    try:
        return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))
    except:
        return 0
