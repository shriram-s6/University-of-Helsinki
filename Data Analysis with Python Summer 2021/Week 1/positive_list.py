#!/usr/bin/env python3

def positive_list(L):
    lst = list(filter(lambda x: x >0, L))
    return lst

def main():
    L=[2,-2,0,1,-7]
    result = positive_list(L)
    print(result)


if __name__ == "__main__":
    main()
