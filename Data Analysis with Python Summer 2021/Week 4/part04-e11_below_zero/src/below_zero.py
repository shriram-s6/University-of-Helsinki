#!/usr/bin/env python3

import pandas as pd

def below_zero():
    data = pd.read_csv('src/kumpula-weather-2017.csv')
    avg_temp = data[data['Air temperature (degC)'] < 0]
    return avg_temp.shape[0]

def main():
    print('Number of days below zero: {}'.format(below_zero()))
    
if __name__ == "__main__":
    main()
