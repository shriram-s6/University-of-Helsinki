#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    rows = [np.expand_dims(row, axis=0) for row in a]
    return rows

def get_column_vectors(a):
    col_list = [np.expand_dims(col, axis=1) for col in a.T]
    return col_list

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
