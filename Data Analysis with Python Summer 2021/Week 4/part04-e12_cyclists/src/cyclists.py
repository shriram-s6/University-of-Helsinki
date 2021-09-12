#!/usr/bin/env python3

from os import sep
import pandas as pd

def cyclists():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    droprow = data.dropna(how='all')
    dropcol = droprow.dropna(axis=1, how='all')
    
    return dropcol


def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
