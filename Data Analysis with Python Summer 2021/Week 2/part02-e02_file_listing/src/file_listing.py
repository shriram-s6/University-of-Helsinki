#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename, 'r') as file:
        file_reader = file.read()
        lst = re.findall(r'.*-all\s+([0-9]+)\s+([A-Za-z]+)\s+(\d+)\s+(\d+):(\d+)\s([A-Za-z._0-9-]+)', file_reader)
        final_list = []
        for each_line in lst:
            (size, month, day, hour, minute, file_name) = each_line
            final_list.append((int(size), month, int(day), int(hour), int(minute), file_name))
    return final_list


def main():
    print(file_listing('listing.txt'))


if __name__ == "__main__":
    main()
