#!/usr/bin/env python3

def main():
    print('\n'.join(['({},{})'.format(num1, num2)for num1 in range(1, 7) for num2 in range(1, 7) if (num1 + num2 == 5)]))

if __name__ == "__main__":
    main()
