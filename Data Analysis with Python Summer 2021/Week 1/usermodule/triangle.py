# Enter you module contents here
import math
import sys

__doc__ = """ This module is used to calculate the Hypothenuse and area of a right angled triangle
"""
__version__ = sys.version
__author__ = 'Shriram S'


def hypothenuse(a, b):
    """ The below function will take length of two sides of a right angled triangle as
 parameters and calculate the length of the hypothenuse"""

    hyp = math.sqrt(a * a + b * b)
    return hyp


def area(height, base):
    """ The below function will take the base and height of a right angled triangle as
 parameters and calculate the area"""
 
    tri_area = (height * base) / 2
    return tri_area
