#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():

    data = pd.read_csv('src/presidents.tsv', delimiter='\t')
    data['Start'] = data['Start'].str.extract(r'(\d{4})')
    new_dtype = {'Start': int, 'Last': float, 'Seasons': int}
    data['Last'].replace('-', np.nan, inplace=True)
    data['Seasons'].replace('two', 2, inplace=True)
    data['Vice-president'] = data['Vice-president'].str.title()
    
    for ind, president in enumerate(data['President'].to_list()):
        if ind > 1:
            first_name, last_name = president.split(', ')
            data.iloc[ind:ind + 1, 0] = last_name + ' ' + first_name

    for ind, president in enumerate(data['Vice-president'].to_list()):
        if ind > 1:
            first_name, last_name = president.split(', ')
            data.iloc[ind:ind + 1, 4] = last_name + ' ' + first_name

    data = data.astype(new_dtype)

    return data

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
