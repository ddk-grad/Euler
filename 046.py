"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

import euler_utils as utils
import math

limit = 10000

primes = set(utils.primes_till(limit))

for number in range(35,limit, 2):
    if number not in primes:
        found = False
        for square in range(1, int(math.sqrt(number/2))+1):
            if (number - (2*square*square)) in primes:
                found = True
                break
        if not found:
            print number
            break





