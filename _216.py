"""
Consider numbers t(n) of the form t(n) = 2n2-1 with n > 1.
The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
For n ? 10000 there are 2202 numbers t(n) that are prime.

How many numbers t(n) are prime for n ? 50,000,000 ?
"""
import time
import math
start_time = time.time()

count = 0
int_is_prime = []

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num
# print("List of Primes is completed")

for x in range(2, 10000):
# for x in range(2, 50000000):
    x = 2*x**2-1
    # if x % 7 == 0:
    #     continue
    if is_prime(x):
        count += 1
print(count)


print("--- %s seconds ---" % (time.time() - start_time))
# input()