"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import time
start_time = time.time()

count = 0
flag = 0
int_is_prime = []

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

def rotate(l, n):
    return l[n:] + l[:n]

for x in range(2, 1000000):
    if is_prime(x):
        int_is_prime.append(x)
print(int_is_prime)
for x in int_is_prime:
    temp = list(str(x))

    if len(temp) < 3:
        if int(''.join(temp[::-1])) in int_is_prime:
            count += 1

    if len(temp) > 2:
        for y in range(1, len(temp)+1):
            temp = rotate(temp, 1)
            flag = 0
            if int(''.join(temp)) not in int_is_prime:
                flag = 1
                break
        if flag == 0:
            count += 1
            flag = 0
            print(''.join(temp))

print("total = ", count)

print("--- %s seconds ---" % (time.time() - start_time))
# input()