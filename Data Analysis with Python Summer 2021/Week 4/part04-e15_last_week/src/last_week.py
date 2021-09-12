#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    data = pd.read_csv('src/UK-top40-1964-1-2.tsv', delimiter='\t')
    data['WoC'] -= 1
    data = data[~data['LW'].isin(['New', 'Re'])]
    data['LW'] = data['LW'].astype(int)

    filter1 = data['Peak Pos'] == data['Pos']
    filter2 = data['Pos'] < data['LW']
    filtered = filter1 & filter2

    data.loc[filtered, 'Peak Pos'] = np.nan
    data = data.sort_values(by=['LW'])
    data.index = data['LW']
    data = data.reindex(range(1, 41))
    data['Pos'] = data.index
    data['LW'] = np.nan
    return data

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
