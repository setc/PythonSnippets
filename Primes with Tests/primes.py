# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Functions to calculate an represent the first n prime numbers.

This module contains functions used to calculate prime numbers and to represent
a multiplication table of these numbers.

Functions:
    is_prime(list_of_primes, number): check if n is prime.
    first_n_primes(n): calculate the first n primes
    mult_table(mult_list): create an array with the multiplication table of
        mult_list
    print_primes_mult_table(n): print the multiplication table of the fist n
        prime numbers
"""

# TODO: Add an argument to the script so it may be run as:
#   !$python primes.py -n, where n is the amout of prime numbers, with 10 as
#   default.

# NOTE: About not using OOP.
# I know is one of the thing this script should show, but the tries I made to
# make an OO approach work where more awkward than just a structured script.
# So I decided to keep it simple over trying to make OO work in this case.

import math
from pandas import DataFrame # Should be replaced by string formatting later


def is_prime(list_of_primes, number):
    """Check if the number given is prime compared to a list of prime numbers.

    Input:
        list_of_primes: list of prime numbers
        number: int
    Output:
        bool, True if prime, false otherwise
    """

    # We are not supposed to pass an even number to this function, so let's
    # put a sanity check here just in case
    assert not number % 2 == 0, "Unexpected even number in function is_prime"

    for prime in list_of_primes:
        if prime <= math.sqrt(number) and number % prime == 0:
            return False

    return True


def first_n_primes(n):
    """Calculate the first n prime numbers.

    Input:
        n: int
    Output:
        primes: list
    """

    # Initial list of primes
    primes = [2, 3]

    # Calculate up to what number we need to check to find the first n
    # prime numbers. The n_estimate formula is only valid if we are looking for
    # 5 or more primes, so we need to cover n = 1, 3 and 4. It already works
    # for n = 2
    if n == 1:
        return [2]
    elif n == 3:
        return [2, 3, 5]
    elif n == 4:
        return [2, 3, 5, 7]
    else:
        n_estimate = int(n * math.log(n) + n * math.log(math.log(n)))

    # An interator is the right choice in this problem, less memory usage
    # and faster than using a list
    candidates = (x for x in range(n_estimate) if x > 3 and not x % 2 == 0)

    for number in candidates:
        if is_prime(primes, number):
            primes.append(number)

    return primes


def mult_table(mult_list):
    """
    Create a list of list containing a 'multiplication table'

    Input: mult_list(list)
    Output: a matrix containing the 'multiplication table'
    """

    # A list comprenhension inside of another
    return [[x * y for y in mult_list] for x in mult_list]


def primes_mult_table(n):
    """
    Pretty print a multiplication table of the first n primes.
    """

    # TODO: Pandas' DataFrame function takes care of a lot of problems for us
    # and is a library we can rely on.
    # As an initial solution it works very well but importing pandas for this
    # script is overkill. Just the importing of takes more time than the
    # prime numbers calculation itself!

    prime_list = first_n_primes(n)
    table = mult_table(prime_list)

    return DataFrame(table, prime_list, prime_list)

def print_mult_table(n):
    """
    Prints the table from primes_mult_table(n).
    """

    # The reason this is a function is to allow arguments in the 'main' section
    # of the script and to avoid side effects in primes_mult_table that would
    # make it harder to test.

    print(primes_mult_table(n))


if __name__ == '__main__':
    print_mult_table(10)
