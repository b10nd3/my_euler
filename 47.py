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
dels = []
count = 0
foundx = 0
secndfndx = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

for x in range(2, 10000):
    if is_prime(x):
        list_of_primes.append(x)

#for 3 primes
# for x in range(1, 1000):
#     foundx = 0
#     for a in list_of_primes:
#         if a > x / 6 or foundx == 1:
#             break
#         for b in list_of_primes:
#             if b > x / (a*2) or foundx == 1:
#                 break
#             for c in list_of_primes:
#                 if c > x / (a*b) or foundx == 1:
#                     break
#                 if x == a*b*c or x==a**2*b*c:# or x==a*b**2*c or x==a*b*c**2:# or x==a**2*b**2*c**2:
#                     tmp_list_of_delit = [a, b, c]
#                     if len(set(tmp_list_of_delit)) == len(tmp_list_of_delit):
#                         foundx = 1
#                         dels.append(x)
#                         dels.append(sorted(tmp_list_of_delit))
#
#                         # print(x, a, b, c, count, tmp_list_of_delit)
#
#                         if x == secndfndx + 1:
#                             count += 1
#                             if count > 1:
#                                 print(f'count = {count}. deliteli: {dels}')
#                         if x != secndfndx + 1:
#                             count = 0
#                             dels = []
#                         secndfndx = x

#for 4 primes
for x in range(1, 1000000):
    foundx = 0
    for a in list_of_primes:
        if a > x / 8 or foundx == 1:
            break
        for b in list_of_primes:
            if b > x / (a*4) or foundx == 1:
                break
            for c in list_of_primes:
                if c > x / (a*b*2) or foundx == 1:
                    break
                for d in list_of_primes:
                    if d > x / (a*b*c) or foundx == 1:
                        break

                    print(f'{x} = {a} * {b} * {c} * {d}')

                    if x == a*b*c*d or x==a**2*b*c*d:# or x==a*b**2*c*d or x==a*b*c**2*d or x==a*b*c*d**2:# or x==a**2*b**2*c**2*d**2:
                        tmp_list_of_delit = [a, b, c, d]

                        if len(set(tmp_list_of_delit)) == len(tmp_list_of_delit):
                            foundx = 1
                            dels.append(x)
                            dels.append(sorted(tmp_list_of_delit))

                            print(x, a, b, c, d, count, tmp_list_of_delit)

                            if x == secndfndx + 1:
                                count += 1
                                if count > 1:
                                    print(f'count = {count}. deliteli: {dels}')
                            if x != secndfndx + 1:
                                count = 0
                                dels = []
                            secndfndx = x

print("--- %s seconds ---" % (time.time() - start_time))
# input()