"""
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ? S for every pair of consecutive primes with 5 ? p1 ? 1000000.
"""
import time
start_time = time.time()

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num

list_of_primes = set()
total = 0
flag = 0
y = 0
count = 0

# for x in range(5, 1000000):
for x in range(5, 100):
    if is_prime(x):
        list_of_primes.add(x)
list_of_primes = sorted(list_of_primes)
print("Set of primes completed")

# for x in range(0, len(list_of_primes) - 1):
#     flag = 0
#     while flag == 0:
#         temp = int(str(y) + str(list_of_primes[x])) / list_of_primes[x+1]
#         if temp.is_integer():
#             total += y
#             print(str(y) + str(list_of_primes[x]),"/", list_of_primes[x+1], temp)
#             flag = 1
#         y += 1
#     y = 1

y = 1
for x in range(0, len(list_of_primes) - 1):
    flag = 0
    while flag == 0:
        temp = list_of_primes[x+1] * y
        temp = str(temp)
        # print(str(list_of_primes[x]), temp, temp[-len(str(list_of_primes[x+1])):])
        if str(list_of_primes[x]) == temp[-len(str(list_of_primes[x+1])):]:
            total += y
            flag = 1
        y += 1
    y = 1



print(total)


print("--- %s seconds ---" % (time.time() - start_time))







