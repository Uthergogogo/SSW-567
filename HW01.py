"""
HW01
Date: 2020-01-26 23:19:49
Author: Zeyu Wu
"""
import unittest


def classify_triangle(a, b, c):
    """ the function to classify a triangle """
    if a < b+c and b < a+c and c < a+b:
        if a == b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isosceles"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "right"
        elif a != b and b != c and a != c:
            return "scalene"

    else:
        return "NotATriangle"


def main():
    """ function to run the code """
    try:
        line1 = float(input("Please enter a number:"))
        line2 = float(input("Please enter a number:"))
        line3 = float(input("Please enter a number:"))
    except ValueError:
        print("There's at least one invalid input.")
    else:
        print(classify_triangle(line1, line2, line3))


class TestTriangle(unittest.TestCase):
    """ test case for triangle """
    def test_isnot_triangle(self):
        """ test whether it's a triangle """
        self.assertEqual(classify_triangle(0.5, 0.5, 1), "NotATriangle")

    def test_equilateral(self):
        """ test whether it's equilateral """
        self.assertEqual(classify_triangle(3, 3, 3), "equilateral")

    def test_isosceles(self):
        """ test whether it's isosceles """
        self.assertEqual(classify_triangle(3, 3, 4), "isosceles")

    def test_scalene(self):
        """ test whether it's scalene """
        self.assertEqual(classify_triangle(3, 2, 4), "scalene")

    def test_right(self):
        """ test whether it's right """
        self.assertEqual(classify_triangle(3, 4, 5), "right")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)





