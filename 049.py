"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import euler_utils as utils


def find_sequence(prime_set): #we can generate a 3-tuple set and see if it is in arithmetic sequence
    for x in prime_set:
        if (x + 3330) in prime_set and (x+2*3330) in prime_set:
            print str(x)+str(x+3330)+str(x+2*3330)
            return True
    return False

primes = set(utils.primes_till(10000))
already_seen = set([])
for x in utils.generate_permutations(str(1487)):
    already_seen.add(int(x))
#print already_seen

for num in range(1001, 10000):
    if num in primes and num not in already_seen:
        already_seen.add(num)
        prime_set= set([])
        for x in utils.generate_permutations(str(num)):
            permutation = int(x)
            if permutation in primes and permutation>1000:
                already_seen.add(permutation)
                prime_set.add(permutation)
        if len(prime_set) > 2:
            found = find_sequence(prime_set)
            if found:
                break
