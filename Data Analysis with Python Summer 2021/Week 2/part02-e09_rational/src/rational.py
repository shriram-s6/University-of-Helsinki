#!/usr/bin/env python3

class Rational(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return '{}/{}'.format(self.first, self.second)

    def __mul__(num1, num2):
        return Rational(num1.first * num2.first, num1.second * num2.second)

    def __truediv__(num1, num2):
        return Rational(num1.first * num2.second, num1.second * num2.first)

    def __add__(num1, num2):
        return Rational(num1.first * num2.second + num2.first * num1.second, num1.second * num2.second)

    def __sub__(num1, num2):
        return Rational(num1.first * num2.second - num2.first * num1.second, num1.second * num2.second)

    def __eq__(num1, num2):
        return num1.first == num2.first and num2.second == num1.second

    def __gt__(num1, num2):
        return num1.first * num2.second > num2.first * num1.second

    def __lt__(num1, num2):
        return num1.first * num2.second < num2.first * num1.second     
           
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
