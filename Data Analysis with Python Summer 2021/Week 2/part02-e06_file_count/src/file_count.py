#!/usr/bin/env python3

import sys
from collections import Counter

def file_count(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return (line_count, word_count, char_count)

def main():
    files = sys.argv[1:]

    for file in files:
        line_count, word_count, char_count = file_count(file)
        print('{}\t{}\t{}\t{}'.format(line_count, word_count, char_count, file))

if __name__ == "__main__":
    main()
