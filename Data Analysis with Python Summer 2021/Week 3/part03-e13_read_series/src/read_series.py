#!/usr/bin/env python3
import pandas as pd

def read_series():
    values = []
    indexes = []

    while True:
        user_input = input("Please enter: ")
        if len(user_input) == 0:
            break
        else:
            input_split = user_input.split()

            if len(input_split) < 2:
                raise Exception
            else:
                indexes.append(input_split[0])
                values.append("".join(input_split[1:]))

    return pd.Series(values, indexes)

def main():
    read_series()

if __name__ == "__main__":
    main()
