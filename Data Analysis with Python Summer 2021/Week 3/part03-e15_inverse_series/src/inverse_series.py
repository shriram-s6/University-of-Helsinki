#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):

    return pd.Series(data=s.index, index=s.values)

def main():
    series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], dtype=int)
    inverse_series(series)

if __name__ == "__main__":
    main()
