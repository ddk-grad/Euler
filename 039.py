"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""



import euler_utils as utils

perimeter_solutions = [0 for x in range(1001)];

for p in range(4, 501):  #I could have written a simpler solution
    for m in range(p,1, -1):
        for n in range(1,m):
            if m*(m+n) > p:
                break
            if not ((m+n)%2 == 1) or not (len(set(utils.prime_factors(m)).intersection(set(utils.prime_factors(n)))) == 0):
                continue
            a = 2*m*n
            b = (m**2)-(n**2)
            c = (m**2)+(n**2)
            if (a**2 + b**2 ) == (c**2) and (a+b+c) == 2*p:
               perimeter = 2*p
               d = perimeter
               while d <= 1000:
                   perimeter_solutions[d] += 1
                   d += perimeter

print perimeter_solutions.index(max(perimeter_solutions))
