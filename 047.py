"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""


import euler_utils as utils
from itertools import groupby


def get_factor_set(number):
    factors = utils.prime_factors(number)
    factors_set = set([])
    for key, value in groupby(factors):
        factors_set.add((key, len(list(value))))
    return factors_set

con_list = []

number = 648

while True:
    if len(con_list) == 4:
        break
    factors_set = get_factor_set(number)
    if len(factors_set) == 4:
        con_list.append(number)
    else:
        con_list=[]
    number += 1

#print factors_dict

print con_list[0]