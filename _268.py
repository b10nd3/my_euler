"""
It can be verified that there are 23 positive integers less than 1000 that are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 1016 are divisible by at least four distinct primes less than 100.
"""
import time
start_time = time.time()

import itertools
import math

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# def is_prime(num):
#     d = 2
#     while d * d <= num and num % d != 0:
#        d += 1
#     return d * d > num
# for x in range(2, 100):
#     if is_prime(x):
#         list_of_primes.append(x)
# print(len(list_of_primes), list_of_primes)

upperlimit = 10**16
# upperlimit = 1000
total = 0

# print(math.factorial(25)/(math.factorial(25-4)*math.factorial(4)))
newlist = list(itertools.combinations(list_of_primes, 4))

for x in newlist:
    # print(x)
    total += (upperlimit // (x[0]*x[1]*x[2]*x[3]))

print(len(newlist), total)

# 12650 1852825865389314

print("--- %s seconds ---" % (time.time() - start_time))
# input()