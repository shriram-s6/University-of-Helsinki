#!/usr/bin/env python3
from collections import Counter

def word_frequencies(filename):
    with open(filename, 'r') as file:
        file_reader = file.readlines()
        word_list = [each.strip("""!"#$%&'()*,-./:;?@[]_""") for line in file_reader for each in line.split()] 
        word_dict = dict(Counter(word_list))
    return word_dict

def main():
    for key, value in word_frequencies('alice.txt').items():
        print('{}\t{}'.format(key, value))

if __name__ == "__main__":
    main()
