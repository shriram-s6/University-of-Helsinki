#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    series1 = pd.Series(L1, index=['a', 'b', 'c'])
    series2 = pd.Series(L2, index=['a', 'b', 'c'])
    return (series1, series2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    s2.drop(index='b', inplace=True)
    return (s1, s2)
    
def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    series1, series2 = create_series(list1, list2)
    s1, s2 = modify_series(series1, series2)

    return s1 + s2 
    
if __name__ == "__main__":
    main()
