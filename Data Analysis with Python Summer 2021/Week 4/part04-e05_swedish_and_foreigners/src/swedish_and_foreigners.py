#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    data = pd.read_csv('src/municipal.tsv', sep='\t')
    data_frame = data[1: 312]
    data_frame.set_index('Region 2018', inplace=True)
    data_frame = data_frame[(data_frame['Share of Swedish-speakers of the population, %'] > 5.0) & (data_frame['Share of foreign citizens of the population, %'] > 5.0)]
    final_df = data_frame.filter(['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %'], axis=1)
    return final_df

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
