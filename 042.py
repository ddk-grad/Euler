"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""


traingle_numbers = set([(i*(i+1))/2 for i in range(1, 1000)])

words = (open('resources/p042_words.txt','r').readlines())[0].split(",")
words = [word.strip('"') for word in words]

count = 0
for word in words:
    if sum(map((lambda x: ord(x)-64), word)) in traingle_numbers:
        count += 1

print count