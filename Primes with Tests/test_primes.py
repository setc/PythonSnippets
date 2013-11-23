# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Test cases for the primes.py module.

This module contain the tests for the primes.py module, testing each function
in primes.py
"""

import primes
import unittest
import pandas


class TestIsPrime(unittest.TestCase):
    """Tests for the funtion is_prime
    """

    def test_is_prime_11(self):
        """Test a prime number.
        """
        self.assertTrue(primes.is_prime([3, 5, 7], 11))

    def test_is_prime_15(self):
        """Test an odd number that is not a prime
        """
        self.assertFalse(primes.is_prime([3, 5, 7], 15))

    def test_is_prime_22(self):
        """Test if is_prime throw an exception when passed an even number as
        argument.
        """
        try:
            primes.is_prime([3, 5, 7, 11], 22)
        except AssertionError:
            pass
        else:
            self.fail('AssertionError for is_prime(22) not thrown')


class TestFirstNPrimes(unittest.TestCase):
    """Test for the function first_n_primes
    """

    # Note, because n_estimate only works for numbers 5 or higher we need to
    # check that all the cases for n = 1, 2, 3, 4 work fine.

    def test_first_10_primes(self):
        """Test an easy case: calculate the first ten primes.
        """
        ten_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        self.assertEqual(primes.first_n_primes(10), ten_primes)

    def test_only_one_prime(self):
        """Test the corner case where only the first prime (2) is requested
        """
        self.assertEqual(primes.first_n_primes(1), [2])

    def test_first_two_primes(self):
        """Test the corner case where only the two frist primes are requested
        """
        self.assertEqual(primes.first_n_primes(2), [2, 3])

    def test_first_three_primes(self):
        """Test the corner case where only the two frist primes are requested
        """
        self.assertEqual(primes.first_n_primes(3), [2, 3, 5])

    def test_first_four_primes(self):
        """Test a middle case, four primes
        """
        self.assertEqual(primes.first_n_primes(4), [2, 3, 5, 7])


class TestMultTable(unittest.TestCase):
    """Test for the mult_table function
    """
    # No need to test a lot here, because the function is functionally pure
    # just two list comprehension nested one inside the other

    def test_mult_table_size_2(self):
        """Test if it makes a matrix of size 2
        """
        test_2 = [1, 2]
        table_of_2 = [[1, 2], [2, 4]]

        self.assertEqual(primes.mult_table(test_2), table_of_2)

    def test_mult_table_size_4(self):
        """Test if it makes a matrix of size 4
        """
        test_4 = [1, 2, 3, 4]
        table_of_4 = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12],
                     [4, 8, 12, 16]]

        self.assertEqual(primes.mult_table(test_4), table_of_4)


class TestPrimesMultTable(unittest.TestCase):
    """Test for primes_mult_table
    """

    # You can't use """ """ strings to make the test, because python will
    # count the spaces used to indent the code making all the assertEqual fail
    # So you need to edit the strings adding the \n parts by hand. Not very
    # hard with small tables.

    def test_pandas_type(self):
        """Test if we are still using DataFrame for this function.
        """
        self.assertIsInstance(primes.primes_mult_table(1),
            pandas.core.frame.DataFrame)

    def test_table_of_1(self):
        """Test a table with only one element
        """
        table_1 = "   2\n2  4"

        self.assertEqual(str(primes.primes_mult_table(1)), table_1)

    def test_table_of_2(self):
        """Test a table with only two elements
        """
        table_2 = "   2  3\n2  4  6\n3  6  9"

        self.assertEqual(str(primes.primes_mult_table(2)), table_2)

    def test_table_of_3(self):
        """Test a table with three elements
        """
        table_3 = "    2   3   5\n2   4   6  10\n3   6   9  15\n5  10  15  25"

        self.assertEqual(str(primes.primes_mult_table(3)), table_3)


if __name__ == '__main__':
    unittest.main()
