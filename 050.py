"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


import euler_utils as utils

limit = 1000000
primes = utils.primes_till(limit)
prime_set = set(primes)

max_prime = 953
max_length = 21

for i in range(len(primes) - 1):
    total = primes[i]
    for j in range(i+1, len(primes)):
        total += primes[j]
        if total >= limit:
            break
        elif total in prime_set:
            length = j-i+1
            if length > max_length:
                max_prime = total
                max_length = length

print max_prime
