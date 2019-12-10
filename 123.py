"""
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn?1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ? 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.
"""
import time
import math
start_time = time.time()


# top = 10**9
top = 10**10

list_of_primes = []
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

for x in range(1, 1000000):
    if is_prime(x):
        list_of_primes.append(x)

print("--- %s seconds ---" % (time.time() - start_time))
print("List of Primes is completed")

# print(list_of_primes)
for x in range(0, len(list_of_primes)-1):
    r = ((list_of_primes[x]-1)**x + (list_of_primes[x]+1)**x) % ((list_of_primes[x]**2))
    if r > top:
        print(x, r)
        input()


print("--- %s seconds ---" % (time.time() - start_time))
# input()