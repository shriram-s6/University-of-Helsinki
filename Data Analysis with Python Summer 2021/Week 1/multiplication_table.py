#!/usr/bin/env python3


def main():
    for num1 in range(1, 11):
        for num2 in range(1, 11):
            print('{:4d}'.format(num1 * num2), end='')
        print()

if __name__ == "__main__":
    main()
