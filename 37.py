"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time
start_time = time.time()


list_of_primes = []
max_summa = 0
count = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


for x in range(2, 1000000):
    if is_prime(x):
        list_of_primes.append(x)
print(list_of_primes)

for x in list_of_primes[6:]:
    temp = list(str(x))
    if len(temp) == 2:
        if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[1:])) in list_of_primes:
                print(x, temp, temp[1:], temp[2:], temp[:1], temp[:2])
                max_summa += x
                count += 1

    if len(temp) == 3:
       if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[:-2])) in list_of_primes:
                if int(''.join(temp[1:])) in list_of_primes:
                    if int(''.join(temp[2:])) in list_of_primes:
                        print(x, temp, temp[1:], temp[2:], temp[:1], temp[:2])
                        max_summa += x
                        count += 1
    if len(temp) == 4:
        if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[:-2])) in list_of_primes:
                if int(''.join(temp[:-3])) in list_of_primes:
                    if int(''.join(temp[1:])) in list_of_primes:
                        if int(''.join(temp[2:])) in list_of_primes:
                            if int(''.join(temp[3:])) in list_of_primes:
                                print(x, temp, temp[1:], temp[2:], temp[3:], temp[:1], temp[:2], temp[:3])
                                max_summa += x
                                count += 1
    if len(temp) == 5:
        if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[:-2])) in list_of_primes:
                if int(''.join(temp[:-3])) in list_of_primes:
                    if int(''.join(temp[:-4])) in list_of_primes:
                        if int(''.join(temp[1:])) in list_of_primes:
                            if int(''.join(temp[2:])) in list_of_primes:
                                if int(''.join(temp[3:])) in list_of_primes:
                                    if int(''.join(temp[4:])) in list_of_primes:
                                        print(x, temp, temp[1:], temp[2:], temp[3:], temp[4:], temp[:1], temp[:2], temp[:3], temp[:4])
                                        max_summa += x
                                        count += 1
    if len(temp) == 6:
        if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[:-2])) in list_of_primes:
                if int(''.join(temp[:-3])) in list_of_primes:
                    if int(''.join(temp[:-4])) in list_of_primes:
                        if int(''.join(temp[:-5])) in list_of_primes:
                            if int(''.join(temp[1:])) in list_of_primes:
                                if int(''.join(temp[2:])) in list_of_primes:
                                    if int(''.join(temp[3:])) in list_of_primes:
                                        if int(''.join(temp[4:])) in list_of_primes:
                                            if int(''.join(temp[5:])) in list_of_primes:
                                                print(x, temp, temp[1:], temp[2:], temp[3:], temp[4:], temp[:1], temp[:2], temp[:3], temp[:4])
                                                max_summa += x
                                                count += 1
    if len(temp) == 7:
        if int(''.join(temp[:-1])) in list_of_primes:
            if int(''.join(temp[:-2])) in list_of_primes:
                if int(''.join(temp[:-3])) in list_of_primes:
                    if int(''.join(temp[:-4])) in list_of_primes:
                        if int(''.join(temp[:-5])) in list_of_primes:
                            if int(''.join(temp[:-6])) in list_of_primes:
                                if int(''.join(temp[1:])) in list_of_primes:
                                    if int(''.join(temp[2:])) in list_of_primes:
                                        if int(''.join(temp[3:])) in list_of_primes:
                                            if int(''.join(temp[4:])) in list_of_primes:
                                                if int(''.join(temp[5:])) in list_of_primes:
                                                    if int(''.join(temp[6:])) in list_of_primes:
                                                        print(x, temp, temp[1:], temp[2:], temp[3:], temp[4:], temp[:1], temp[:2], temp[:3], temp[:4])
                                                    max_summa += x
                                                    count += 1
print(count, max_summa)


print("--- %s seconds ---" % (time.time() - start_time))
# input()