"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import time
start_time = time.time()


import itertools
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num

numbers = "1234567"
numbers = sorted(list(itertools.permutations(numbers)))
for x in numbers:
    x = int(''.join(x))
    if is_prime(x):
        print(x)

print("--- %s seconds ---" % (time.time() - start_time))
# input()