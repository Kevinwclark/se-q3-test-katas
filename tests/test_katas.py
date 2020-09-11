import unittest
import katas
import random


__author__ = 'Kevin Clark with help from Joseph Hafed and Daniel Lomelino'


class TestKatas(unittest.TestCase):
    """tests the add function"""
    def test_add(self):
        x = random.randrange(-10, 10)
        y = random.randrange(-10, 10)
        s = x + y
        self.assertEqual(katas.add(x, y), s)

    def test_multiply(self):
        """tests the multiply function"""
        x = random.randrange(-10, 10)
        y = random.randrange(-10, 10)
        s = x * y
        self.assertEqual(katas.multiply(x, y), s)

    def test_power(self):
        """tests the power function"""
        self.assertEqual(katas.power(2, 2), 4)
        with self.assertRaises(ValueError):
            katas.power(2, -1)
        with self.assertRaises(ValueError):
            katas.power(2, 0.2)

    def test_factorial(self):
        """tests the factorial function"""
        terms = [
            1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
            479001600, 6227020800, 87178291200, 1307674368000
        ]
        for index, element in enumerate(terms, 1):
            self.assertEqual(katas.factorial(index), element)
        with self.assertRaises(ValueError):
            katas.factorial(-3)

    def test_fibonacci(self):
        """tests the fibonacci function"""
        terms = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181,
            6765, 10946, 17711, 28657, 46368, 75025,
            121393, 196418, 317811, 514229
        ]
        for index, element in enumerate(terms):
            self.assertEqual(katas.fibonacci(index), element)
        with self.assertRaises(ValueError):
            katas.fibonacci(-3)


if __name__ == '__main__':
    unittest.main()
