#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):

    municipalities = df.shape[0]
    growing_df = df[df['Population change from the previous year, %'] > 0]
    population_increase = growing_df.shape[0]
    proportion = population_increase / municipalities
    return proportion

def main():
    data = pd.read_csv('src/municipal.tsv', sep='\t')
    data_frame = data[1: 312]
    data_frame.set_index('Region 2018', inplace=True)
    print('Proportion of growing municipalities: {:.1f}%'.format(growing_municipalities(data_frame) * 100))

if __name__ == "__main__":
    main()
