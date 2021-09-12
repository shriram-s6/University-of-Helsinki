#!/usr/bin/env python3

import pandas as pd


def split_date():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    data = data.dropna(how='all')
    data = data.dropna(axis=1, how='all')

    data[['Weekday', 'Day', 'Month', 'Year', 'Hour']] = data['Päivämäärä'].str.split(' ', n=5, expand=True)

    data.replace({'Weekday': {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun'
    }}, inplace=True)

    data.replace({
        'Month': {
            'tammi': 1,
            'helmi': 2,
            'maalis': 3,
            'huhti': 4,
            'touko': 5,
            'kesä': 6,
            'heinä': 7,
            'elo': 8,
            'syys': 9,
            'loka': 10,
            'marras': 11,
            'joulu': 12
        }
    }, inplace=True)

    data['Hour'] = data['Hour'].str[0:2].map(int)
    
    new_data = data.iloc[:, -5:]

    new_data['Day'] = new_data['Day'].map(int)
    new_data['Year'] = new_data['Year'].map(int) 

    return new_data


def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
