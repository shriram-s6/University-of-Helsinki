#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        valid_shapes = ['triangle', 'rectangle', 'circle']
        shape = input('Choose a shape from triangle, rectangle, circle: ')
        if not shape:
            break
        elif shape not in valid_shapes:
            print('Unknown shape!')
        
        if shape == 'triangle':
            base = int(input('Enter base of the triangle: '))
            height = int(input('Enter height of the triangle: '))
            print('The area is {:.6f}'.format(base * height * 0.5))
        
        if shape == 'rectangle':
            width = int(input('Enter width of the rectangle: '))
            height = int(input('Enter height of the rectangle: '))
            print('The area is {:.6f}'.format(width * height))
        if shape == 'circle':
            radius = int(input('Enter radius of the circle: '))
            print('The area is {:.6f}'.format(math.pi * radius **2 ))

if __name__ == "__main__":
    main()
