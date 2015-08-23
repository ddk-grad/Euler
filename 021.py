"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import euler_utils as utils

no_op_set = set(utils.primes_till(10000))

dn_map = {}
amicable_pairs = []

dn = lambda x:sum(utils.divisors_of(x))

for num in range(4,10001):
    if num not in no_op_set and num not in dn_map:
        dsum = dn(num)
        dn_map[num] = dsum
        if dsum < 10000 and dsum > num:
            dsum_sum = dn(dsum)
            if dsum_sum == num:
                amicable_pairs.append((num, dsum))
            dn_map[dsum] = dsum_sum

print sum([x+y for x,y in amicable_pairs])


