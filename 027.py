"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

import euler_utils as utils

primes = set(utils.primes_till(1000000))

max_length = 0
max_a = 0
max_b = 0

for a in range(-999,1000, 2):
    for b in range(-999, 1000, 2): # observation b should be prime when n = 0, we can limit b to prime set less than 1000
        f = lambda x: x*(x+a) + b
        n = 0
        length = 0
        while True:
            if f(n) in primes:
                length += 1
                n += 1
            else:
                break
        if length > max_length:
            max_length = length
            max_a = a
            max_b = b

print max_a * max_b

