#!/usr/bin/env python3

def extract_numbers(s):
    final_num = []
    for num in s.split():
        try:
            final_num.append(int(num))

        except ValueError:
            try:
                final_num.append(float(num))
            except ValueError:
                pass

    return final_num

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
