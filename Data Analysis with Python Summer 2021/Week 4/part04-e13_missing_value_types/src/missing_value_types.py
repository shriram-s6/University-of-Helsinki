#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    year = [None, 1917, 1776, 1523, None, 1992]
    president = [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']

    df = pd.DataFrame({'Year of independence': year, 'President': president}, index=state)
    df.index.name  = 'State'
    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
