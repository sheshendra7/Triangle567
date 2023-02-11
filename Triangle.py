# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: sheshendra desiboyina
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Check for Triangle Property : The sum of the length of the two sides
    # of a triangle is greater than the length of the third side.
    if ((a ** 2 + b ** 2) == c ** 2) or ((a ** 2 + c ** 2) == b ** 2) or ((b ** 2 + c ** 2) == a ** 2):
        return 'Right'
    elif (a == b) or (b == c) or (a == c):
        if (a == b == c):
            return 'Equilateral'
        else:
            return 'Isosceles'
    elif (a + b) >= c and (b + c) >= a and (c + a) >= b:
        return 'NotATriangle'
    elif (a != b != c):
        return 'Scalene'
