"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import time
start_time = time.time()

total = 0
sum = 0
int_is_prime = []

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

for x in range(3, 100000):
    sum = 0
    y = list(str(x))
    for i in y:
        sum += factorial(int(i))
    if sum == x:
        # print(x)
        total += sum

print(total)
print("--- %s seconds ---" % (time.time() - start_time))
# input()