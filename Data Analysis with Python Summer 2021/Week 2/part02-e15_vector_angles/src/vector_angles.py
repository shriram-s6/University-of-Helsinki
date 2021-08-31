#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    length = X.shape[0]
    arr = np.zeros((length))

    for i in range(length):
        arr[i] = (np.dot(X[i], Y[i]) / scipy.linalg.norm(X[i]) / scipy.linalg.norm(Y[i]))
    clipped = np.clip(arr, -1, 1)
    angles = np.arccos(clipped)

    return np.degrees(angles)

def main():
    arr_one = np.array([[0, 0, 1], [-1, 1, 0]])
    arr_two = np.array([[0, 1, 0], [1, 1, 0]])

    print(vector_angles(arr_one, arr_two))

if __name__ == "__main__":
    main()
