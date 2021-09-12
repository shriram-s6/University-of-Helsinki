#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    data = pd.read_csv('src/kumpula-weather-2017.csv')
    return data['Snow depth (cm)'].max()

def main():
    print('Max snow depth:', snow_depth())

if __name__ == "__main__":
    main()
