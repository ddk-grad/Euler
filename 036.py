"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


count = 0

for num in range(1,10**6,2): #only consider odd numbers because binary odd number has to end in 1 bit
    num_str = str(num)
    if num_str == num_str[::-1]:
        binary = bin(num)[2:]
        if binary == binary[::-1]:
            count += num

print count
