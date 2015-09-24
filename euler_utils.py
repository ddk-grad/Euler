__author__ = 'dhinesh'

import math
import operator

def primes_till(limit):
    sieve = [True for x in range(limit +1)]
    sieve [0] = False
    sieve[1] = False
    #just eliminate all even numbers
    for x in range(4, limit+1, 2):
        sieve[x] = False
    #consider only odd products of odd prime numbers
    for num in range(3,int(math.sqrt(limit-1)),2):
        if sieve[num]:
            for p in range(3, limit/num + 1, 2):
                sieve[num * p] = False
    return [x for x in range(len(sieve)) if sieve[x]]

def divisors_of(number):
    divisors = [1]
    for i in range(2, int(math.sqrt(number))+1, 1):
        if number % i == 0:
            divisors.append(i)
            second_number = number/i
            if second_number != i:
              divisors.append(second_number)
    return divisors

def factorial_of(number):
  if number < 2:
    return 1
  else:
    answer = 1
    for i in range(2,number+1):
      answer *= i
  return answer

def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number = number/divisor
        else:
            divisor += 1
    return factors

def remove_from_list(a, b):
    for x in b:
        if x in a:
            a.remove(x)
    return a

def prod(factors):
    return reduce(operator.mul, factors, 1)


