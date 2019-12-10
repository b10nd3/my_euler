"""
A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
Including the number 1, there are 29 square root smooth numbers not exceeding 100.

How many square root smooth numbers are there not exceeding 10000000000?
"""
import time
import math
start_time = time.time()


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


list_of_primes = set()
count = 1
flag = 0
temp = 0
for x in range(1, int(math.sqrt(10000000000))):
# for x in range(1, int(math.sqrt(10000))):
    if is_prime(x):
        list_of_primes.add(x)
list_of_primes = sorted(list_of_primes)
print("Set of primes completed")

# for num in range(1, int(math.sqrt(10000000000))):
# for num in range(1, 10000000001):
for num in range(1, 101):
    sqroot = math.sqrt(num)
    for y in list_of_primes:
        if num % y == 0 and y >= sqroot:
            flag = 1
    if flag == 0:
        count += 1
        # print(count, num, sqroot, temp)
    flag = 0
print(count)


#
# count = 1
# flag = 0
# list_of_numbers = [1]
#
# # for num in range(1, 10000000001):
# # for num in range(1, 1000001):
# for num in range(1, 101):
#     if is_prime(num):
#         continue
#     list_of_primes = []
#     sqroot = math.sqrt(num)
#     for x in range(1, int(num / 2 + 1)):
#         if num % x == 0 and is_prime(x):
#             list_of_primes.append(x)
#     for y in list_of_primes:
#         if y >= sqroot:
#             flag = 1
#     if flag == 0:
#         count += 1
#         list_of_numbers.append(num)
#
#     flag = 0
#     print(num, list_of_primes, sqroot)
# print(count)
# print(count, list_of_numbers)

print("--- %s seconds ---" % (time.time() - start_time))







