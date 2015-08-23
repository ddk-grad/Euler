"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

names = [x.strip('"') for x in open('resources/names.txt','r').read().split(",")]
names.sort()

total = 0
count = 1

sum_of_chars = lambda name:sum([ord(c)-64 for c in name])

for name in names:
    total += count * sum_of_chars(name)
    count += 1

print total