"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import euler_utils as utils

factorials = [utils.factorial_of(i) for i in range(0,10)]

total_sum = 0

for i in range(10,7*utils.factorial_of(9)):
    if i == sum([factorials[int(d)] for d in str(i)]):
        total_sum += i

print total_sum