#!/usr/bin/env python3

def sum_equation(L):
    lst = L
    if len(L) > 0:
        sum_eq = ' '.join([' + '.join([str(i) for i in lst])]), '=', sum(lst)
        return ' '.join(str(val) for val in sum_eq)
    else:
        return ' '.join(str(val) for val in [len(lst), '=', len(lst)])

def main():
    L = [1,5,7]
    result = sum_equation(L)
    print(result)

if __name__ == "__main__":
    main()
