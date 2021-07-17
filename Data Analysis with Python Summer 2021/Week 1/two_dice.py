#!/usr/bin/env python3

def main():
    for num1 in range(1, 7):
        for num2 in range(1, 7):
            if num1 + num2 == 5:
                print('({}, {})'.format(str(num1), str(num2)))

if __name__ == "__main__":
    main()
