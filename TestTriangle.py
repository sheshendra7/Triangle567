# -*- coding: utf-8 -*-
"""
Updated Feb 10,2023
The primary goal of this file is to demonstrate a simple unittest implementation
@author: sheshendra desiboyina
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(3, 4, 0), 'InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(-1, -4, 5), 'InvalidInput')

    def testNotATriangle3(self):
        self.assertNotEqual(classifyTriangle(10, 2, 3), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'NotATriangle')

    def testNotATriangle5(self):
        self.assertNotEqual(classifyTriangle(5, 5, 8), 'NotATriangle')

    def testRightTriangle6(self):
        self.assertNotEqual(classifyTriangle(11, 11, 10), 'Right')

    def testEquilateralTriangle7(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def testEquilateralTriangles8(self):
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral')

    def testIsoscelesTriangle9(self):
        self.assertEqual(classifyTriangle(4, 4, 5), 'Isosceles')

    def testIsoscelesTriangle10(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles')

    def testTriangle11(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')

    def testTriangle12(self):
        self.assertEqual(classifyTriangle(4, 8, 10), 'NotATriangle')

    def testTriangle13(self):
        self.assertEqual(classifyTriangle(5, 9, 11), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

