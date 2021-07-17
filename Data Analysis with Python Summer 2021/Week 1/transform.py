#!/usr/bin/env python3

def transform(s1, s2):
    l1 = [int(num) for num in s1.split()]
    l2 = [int(num) for num in s2.split()]
    lst = list(map(lambda x: x[0]*x[1], zip(l1, l2)))
    return lst

def main():
    s1 = "1 5 3"
    s2 = "2 6 -1"
    result = transform(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
