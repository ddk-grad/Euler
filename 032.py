"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

digits = set(['1','2','3','4','5','6','7','8','9'])

def is_pandigital(a,b,c):
    numbers = list(str(a)+str(b)+str(c))
    return len(numbers) == 9 and set(numbers) == digits

product_set = set()

for i in range(1,10):
    for j in range(999,10000):
        product = i*j
        if is_pandigital(i, j, product):
            product_set.add(product)

for i in range(10, 100):
    for j in range(100, 1000):
        product = i*j
        if is_pandigital(i, j, product):
            product_set.add(product)


print sum(list(product_set))