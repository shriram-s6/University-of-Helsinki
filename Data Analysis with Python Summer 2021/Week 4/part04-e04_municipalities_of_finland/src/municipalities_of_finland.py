#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    data = pd.read_csv('src/municipal.tsv', sep='\t')
    data_frame = data[1: 312]
    data_frame.set_index('Region 2018', inplace=True)

    return data_frame
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
