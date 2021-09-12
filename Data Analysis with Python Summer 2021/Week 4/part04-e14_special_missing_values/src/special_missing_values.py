#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    data = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    data.replace({'LW': {'New': None, 'Re': None}}, inplace=True)
    data['LW'] = pd.to_numeric(data['LW'])
    data = data[data['Pos'] > data['LW']]
    return data

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
