#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename, 'r') as file:
        next(file)
        file_reader = file.read()
        lst = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)', file_reader)
        color_list = []
        for tup in lst:
            red, green, blue, color = tup
            color_list.append('{}\t{}\t{}\t{}'.format(red, green, blue, color))
    return color_list


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
