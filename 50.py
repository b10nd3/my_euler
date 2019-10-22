import time
start_time = time.time()

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

list_of_primes = []

max = 0
max_summa = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


for x in range(2, 10000):
    if is_prime(x):
        list_of_primes.append(x)

# print(list_of_primes)

for x in range(0, len(list_of_primes)):
    summa = 0
    count = 0
    for y in range(x, len(list_of_primes)):
        summa += int(list_of_primes[y])
        count += 1
        # print(x, count, summa)
        if is_prime(summa):
            if max < count and summa < 1000000:
                max = count
                max_summa = summa
        if not is_prime(y):
            continue

print(max, max_summa)

print("--- %s seconds ---" % (time.time() - start_time))
input()

