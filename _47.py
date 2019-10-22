"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 ? 7
15 = 3 ? 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2? ? 7 ? 23
645 = 3 ? 5 ? 43
646 = 2 ? 17 ? 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import time
start_time = time.time()

list_of_primes = []
newlist = []
count = 0
flag = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

def find_prime(num):
    for x in list_of_primes:
        if num % x == 0:
            return(x)
    return(False)

for x in range(2, 100000):
    if is_prime(x):
        list_of_primes.append(x)

print(list_of_primes)

for x in range(1, 100000):
    temp = []
    count = 0
    m = x
    while count < 4:
        if find_prime(x):
            y = find_prime(x)
            x = int(x/y)
            count += 1
            temp.append(y)
        else:
            break
    if count == 4:
        newlist = []
        for i in temp:
            if i not in newlist:
                newlist.append(i)

        newlist.sort()
        # print(newlist)
        if len(newlist) == 4:
            flag += 1
        else:
            flag = 0
        if flag == 4:
            print(m, newlist, count, flag)

print("--- %s seconds ---" % (time.time() - start_time))
# input()