#!/usr/bin/env python3

def interleave(*lists):
    lst = []
    for i in zip(*lists):
        lst.extend(i)

    return lst

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
