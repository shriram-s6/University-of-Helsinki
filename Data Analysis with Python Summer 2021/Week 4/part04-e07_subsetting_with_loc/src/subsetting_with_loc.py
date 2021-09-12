#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    data = pd.read_csv('src/municipal.tsv', sep='\t')
    data_frame = data[1: 312]
    data_frame.set_index('Region 2018', inplace=True)
    final_df = data_frame.loc['Akaa': 'Äänekoski', ['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return final_df

def main():
    
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()
