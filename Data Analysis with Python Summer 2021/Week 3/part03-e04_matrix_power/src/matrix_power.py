#!/usr/bin/env python3
import numpy as np
from functools import reduce
import math

def matrix_power(a, n):

    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    else:
        gen = (a for i in range(abs(n)))
        func = lambda x, y: x@y

        multiplied = reduce(func, gen)

        if n > 0:
            return multiplied
        else:
            return np.linalg.inv(multiplied)
    

def main():
    arr = np.array([[0, 1], [-1, 0]])
    print(matrix_power(arr, -3))

if __name__ == "__main__":
    main()
