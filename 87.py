"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
import time
import math
import itertools
start_time = time.time()

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num

max_summ = 50000000
list_of_primes = []
list_of_maching_numbers = []
newlist = []
max1 = int(math.sqrt(max_summ))+9

for x in range(2, max1):
    if is_prime(x):
        list_of_primes.append(x)
for a in list_of_primes:
    for b in list_of_primes:
        if int(a)**2 + int(b)**3 + 16 > max_summ:
            break
        for c in list_of_primes:
            temp = int(a) ** 2 + int(b) ** 3 + int(c) ** 4
            if temp > max_summ:
                break
            else:
                list_of_maching_numbers.append(temp)
for i in list_of_maching_numbers:
  if i not in newlist:
    newlist.append(i)

newlist.sort()
# print(newlist)
print(len(newlist))

print("--- %s seconds ---" % (time.time() - start_time))
# input()