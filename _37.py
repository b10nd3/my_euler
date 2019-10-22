"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time
start_time = time.time()

sum = 0
list_of_primes = []
max_summa = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


for x in range(9, 10000):
    if is_prime(x):
        list_of_primes.append(x)
print(list_of_primes)

for x in list_of_primes:
    temp = list(str(x))
    if int(''.join(temp[:-1])) in list_of_primes:
        print(x)
    # if len(temp) < 3:
    #     if int(''.join(temp[:-1])) in list_of_primes:
    #         count += 1
    #
    # if len(temp) > 2:
    #     for y in range(1, len(temp)+1):
    #         temp = rotate(temp, 1)
    #         flag = 0
    #         if int(''.join(temp)) not in int_is_prime:
    #             flag = 1
    #             break
    #     if flag == 0:
    #         count += 1
    #         flag = 0
    #         print(''.join(temp))






print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
# input()