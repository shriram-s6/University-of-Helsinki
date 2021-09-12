#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    data = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    top_10 = data.iloc[0: 10, [2, 3]]
    return top_10

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
