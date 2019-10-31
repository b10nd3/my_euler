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
flag2 = 0
temp = 0
list_of_fine = []

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

for x in range(2, 1000):
    if is_prime(x):
        list_of_primes.append(x)

# print(list_of_primes)

for x in range(1, 10000000):
    foundx = 0
    for a in list_of_primes:
        if a > int(x / 210) or foundx == 1:
            break
        for b in list_of_primes:
            if b > int(x / a) or foundx == 1:
                break
            for c in list_of_primes:
                if c > int(x / (2*a*b)) or foundx == 1:
                    break
                for d in list_of_primes:
                    if d > int(x / (a*b*c)) or foundx == 1:
                        break
                    if x == a*b*c*d or x == a**2*b*c*d or x == a*b**2*c*d or x==a*b*c**2*d or x==a*b*c*d**2:
                        if len(dels) == 1:
                            print(f'{x} = {a} * {b} * {c} * {d}. ')
                            list_of_fine.append(string)
                            if f'{x} = {a} * {b} * {c} * {d}' not in list_of_fine:
                                list_of_fine.append(f'{x} = {a} * {b} * {c} * {d}')
                            tmp_list_of_delit = [a, b, c, d]
                            if sorted(tmp_list_of_delit) not in dels:
                                dels.append(sorted(tmp_list_of_delit))
                            print(dels, list_of_fine)

                        # if len(dels) == 2:
                        #     if f'{x} = {a} * {b} * {c}' not in list_of_fine:
                        #         list_of_fine.append(f'{x} = {a} * {b} * {c}')
                        #     tmp_list_of_delit = [a, b, c]
                        #     if sorted(tmp_list_of_delit) not in dels:
                        #         dels.append(sorted(tmp_list_of_delit))
                        #     continue
                        # if len(dels) == 2:
                        #     print(dels, list_of_fine)
                        #     continue

                        string = f'{x} = {a} * {b} * {c} * {d}'
                        tmp_list_of_delit = [a,b,c,d]
                        dels.append(sorted(tmp_list_of_delit))
                        foundx = 1
                    # else:
                        # dels = []
                        # list_of_fine = []
                        # foundx = 0


print("--- %s seconds ---" % (time.time() - start_time))
# input()