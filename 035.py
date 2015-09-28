"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""


import euler_utils as utils

primes = set(utils.primes_till(1000000))

count = 0

for num in primes:
    num_str = str(num)
    if all([x in primes for x in [int(num_str[i:]+num_str[:i])
                                  for i in range(len(num_str))]]):
        count += 1

print count