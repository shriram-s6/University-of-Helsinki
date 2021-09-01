#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    unique_elements = np.unique(a[:, c], axis=0, return_counts=True)
    unique_values, unique_count = unique_elements
    count = np.argsort(-unique_count)
    sorted_values = unique_values[count].reshape((1, -1))
    ind = np.concatenate([np.where((a[:, c] == x))[0] for x in np.nditer(sorted_values)])

    return a[ind]

def main():
    pass

if __name__ == "__main__":
    main()
