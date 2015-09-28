"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import euler_utils as utils

primes = set(utils.primes_till(1000000))

total_sum = 0

for num in primes:
    num_str = str(num)
    if num > 7:
        if all([int(num_str[i:]) in primes for i in range(1,len(num_str))]) and \
                all([int(num_str[:-i]) in primes for i in range(1,len(num_str))]):
            total_sum += num

print total_sum
