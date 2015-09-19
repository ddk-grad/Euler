"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

import euler_utils as utils

digits = [chr(i+48) for i in range(0,10)]

count = 0
permutation = []

for position in range(9,0,-1):
  #we could have just divided here, it will straightaway give us the index
  factorial = utils.factorial_of(position)
  for i in range(len(digits)):
    count += factorial
    if count >= 1000000:
      count -= factorial 
      permutation.append(digits[i])
      digits.remove(digits[i])
      break

permutation = permutation + digits

print ''.join(permutation)




