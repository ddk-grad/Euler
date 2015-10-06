"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

max_pandigital = 0


for num in range(1, 10000):
  num_str = str(num)
  n = 2
  while len(num_str) < 9:
    num_str += str(num * n)
    n += 1
  num_set = set(num_str)
  if len(num_str) == 9 and len(num_set) == 9 and '0' not in num_set:
    pandigital = int(num_str)
    if pandigital > max_pandigital:
      max_pandigital = pandigital

print max_pandigital
