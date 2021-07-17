#!/usr/bin/env python3
from collections import defaultdict


def reverse_dictionary(d):
    rev_dict = defaultdict(list)
    for key, value in d.items():
        for val in value:
            rev_dict[val].append(key)
    return dict(rev_dict)


def main():
    d={"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six":["kuusi"], "fir":["kuusi"]}
    rev_dict = reverse_dictionary(d)
    print(rev_dict)


if __name__ == "__main__":
    main()
