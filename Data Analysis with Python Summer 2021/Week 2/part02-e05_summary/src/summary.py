#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    num_list = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                num_list.append(float(line))
                
            except ValueError:
                pass
    print(num_list)
    total = sum(num_list)
    avg = statistics.mean(num_list)
    stddev = statistics.stdev(num_list)

    return (total, avg, stddev)
    

def main():
    files = sys.argv[1:]
    

    for file in files:
        total, avg, stddev = summary(file)
        print('File: {} Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}'.format(file, total, avg, stddev))
        
        
if __name__ == "__main__":
    main()

