#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    lst = re.findall(r'\[\s*([-+]?\d+)\s*\]', s)
    return [int(i) if len(lst) > 0 else '' for i in lst]

def main():
    sentence = "  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(sentence))

if __name__ == "__main__":
    main()
