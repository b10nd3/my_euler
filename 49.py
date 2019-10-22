"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import time
start_time = time.time()

count = 0
num = 0
int_is_prime = []
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

for x in range(1000, 10000):
    if is_prime(x):
        int_is_prime.append(x)
print(int_is_prime)
for x in int_is_prime:
    temp = x + 3330
    if sorted(str(x)) == sorted(str(temp)):
        print(x, temp)

# 148748178147
# 259359239253
# 148348138143
# 296962999629

print("--- %s seconds ---" % (time.time() - start_time))
input()