#!/usr/bin/env python3

def distinct_characters(L):
    dist_char = {}
    for each in L:
        dist_char[each] = len(set(each))
        
    return dist_char

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
