#!/usr/bin/env python3


def detect_ranges(L):
    lst = sorted(L)
    l1 = []
    l2 = []

    for i in range(len(L) - 1):
        if lst[i] + 1 == lst[i + 1]:
            l1.append(lst[i])
            # checking if the next element is the last element.
            # replacing consecutive elements by pair
            if lst[i + 1] == lst[-1]:
                l2.append((l1[0], lst[i + 1] + 1))
        else:
            if l1:
                l2.append((l1[0], lst[i] + 1))
                l1 = []
            else:
                l2.append(lst[i])
            # if i is the second last element, append the last element and end the operation
            if lst[i + 1] == lst[-1]:
                l2.append(lst[i + 1])

    return l2


def main():
    L = [1, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
