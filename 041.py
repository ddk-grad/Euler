"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


import euler_utils as utils

primes = utils.primes_till((10**7))

ndigit = [str(i) for i in range(1,10)]
#print ndigit

for i in range(len(primes)-1, 1, -1):
    number_str = str(primes[i])
    length = len(number_str)
    if len(set(number_str).intersection(set(ndigit[0:length]))) == length:
        print primes[i]
        break

