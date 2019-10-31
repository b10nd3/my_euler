"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2?12
15 = 7 + 2?22
21 = 3 + 2?32
25 = 7 + 2?32
27 = 19 + 2?22
33 = 31 + 2?12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import time
start_time = time.time()


list_of_primes = []

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


for x in range(2, 100000):
    if is_prime(x):
        list_of_primes.append(x)
for x in range(2, 100000):
    if x % 2 != 0 and x not in list_of_primes:
        flag = 0
        for y in list_of_primes:
            if y > x:
                break
            for z in range(0, 39):
                temp = y + 2 * z ** 2
                if x == temp:
                    flag = 1
                    break
        if flag == 0:
            print(x)



print("--- %s seconds ---" % (time.time() - start_time))
#input()