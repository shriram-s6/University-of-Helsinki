#!/usr/bin/env python3

def find_matching(L, pattern):
    lst = [i for i, char in enumerate(L) if pattern in char]
    return lst

def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)

if __name__ == "__main__":
    main()
