#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    minus_b = -b
    second_part =  math.sqrt(b **2 - 4 * a * c)
    two_a = 2 * a 
    solution_one = (minus_b + second_part) / two_a
    solution_two = (minus_b - second_part) / two_a
    return (solution_one,solution_two)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution_one, solution_two = solve_quadratic(a, b, c)
    print('({:.1f},{:.1f})'.format(solution_one, solution_two))

if __name__ == "__main__":
    main()
