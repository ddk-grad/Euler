"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

indexes = [int(9*(10**(i-1))*i) for i in range(0,7)]
digit_indexes = [10**i for i in range(0,7)]

product = 1
curr_index = 1
sum = 0
for i in range(1, len(indexes)):
    while curr_index < len(digit_indexes) and digit_indexes[curr_index] <= indexes[i]+sum:
        number = digit_indexes[curr_index] - sum - 1;
        digit = int(str(number/i + (10**(i-1)))[(number%i)])
        product *= digit
        curr_index += 1
    if curr_index >= len(digit_indexes):
        break
    sum += indexes[i]

print product

