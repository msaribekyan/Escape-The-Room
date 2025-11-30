# Write a function diagonal_product(arr: np.ndarray) -> int that returns the product of the diagonal of a 3x3 NumPy array.

import numpy as np

def diagonal_product(arr: np.ndarray):
    try:
        if arr.shape != (3,3):
            return 0 # arr is not a 3x3 matrix
        product = 1
        for i in range(3):
            product = product * arr[i][i]
        return product
    except:
        return 0 # arr is not a numpy object

# Example: [[1,2,3],[4,5,6],[7,8,9]] returns 45.
print(diagonal_product(np.array([[1,2,3],[4,5,6],[7,8,9]])))


