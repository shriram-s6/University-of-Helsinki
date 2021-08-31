#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    arr_one = np.arange(n)
    arr_two = np.arange(n).reshape((n, 1))
    return arr_one * arr_two

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
