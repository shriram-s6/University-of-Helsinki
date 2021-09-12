#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    data = pd.read_csv('src/kumpula-weather-2017.csv')
    avg_temp = data[data['m'] == 7]
    return avg_temp['Air temperature (degC)'].mean()

def main():
    print('Average temperature in July: {:.1f}'.format(average_temperature()))

if __name__ == "__main__":
    main()
