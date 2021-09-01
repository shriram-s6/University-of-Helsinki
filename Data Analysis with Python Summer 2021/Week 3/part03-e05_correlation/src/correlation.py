#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data_loaded = load()
    sepal_length = data_loaded[:, 0]
    petal_length = data_loaded[:, 2]

    return (scipy.stats.pearsonr(sepal_length, petal_length)[0])


def correlations():
    data_loaded = load()
    matrix = np.corrcoef(data_loaded, rowvar=False)

    return (matrix)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
