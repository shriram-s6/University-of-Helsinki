#!/usr/bin/env python3

import numpy as np

def diamond(n):
    arr1 = np.fliplr(np.eye(n, dtype=int))
    arr2 = np.eye(n, n-1, k=-1, dtype=int)
    arr3 = np.eye(n-1, n, k=1, dtype=int)
    arr4 = np.fliplr(np.eye(n-1, k=1, dtype=int))

    upper_half = np.concatenate((arr1, arr2), axis=1)
    lower_half = np.concatenate((arr3, arr4), axis=1)

    return (np.concatenate((upper_half, lower_half)))

def main():
    pass

if __name__ == "__main__":
    main()
