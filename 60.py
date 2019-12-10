"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import time
start_time = time.time()

big_list_of_primes = set()
small_list_of_primes = set(["3", "7"])

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

for x in range(8, 10000):
    if is_prime(x):
        small_list_of_primes.add(str(x))
print("--- %s seconds ---" % (time.time() - start_time))
print("First Set of Primes is completed")

# for x in range(2, 1000000):
for x in range(2, 100000000):
    if is_prime(x):
        big_list_of_primes.add(str(x))
print("--- %s seconds ---" % (time.time() - start_time))
print("Second Set of Primes is completed")

for a in small_list_of_primes:
    for b in small_list_of_primes:
        if a+b not in big_list_of_primes or b+a not in big_list_of_primes:
            continue
        for c in small_list_of_primes:
            if a+c not in big_list_of_primes or c+a not in big_list_of_primes or b+c not in big_list_of_primes or c+b not in big_list_of_primes:
                continue
            for d in small_list_of_primes:
                # print(a, b, c, d, temp)
                if a+d not in big_list_of_primes or d+a not in big_list_of_primes or b+d not in big_list_of_primes or d+b not in big_list_of_primes or c+d not in big_list_of_primes or d+c not in big_list_of_primes:
                    continue
#for 4 numbers
                # temp = [a+b, b+a, a+c, c+a, a+d, d+a, b+c, c+b, b+d, d+b, c+d, d+c]
                # flag = 1
                # for i in temp:
                #     if i not in big_list_of_primes:
                #         flag = 0
                # if flag == 1:
                #     sum = int(a)+int(b)+int(c)+int(d)
                #     print(f'sum of {a}, {b}, {c}, {d} is {sum}')
                #     print("--- %s seconds ---" % (time.time() - start_time))
# for 5 numbers
                for e in small_list_of_primes:
                    if a+e not in big_list_of_primes or e+a not in big_list_of_primes:
                        continue
                    temp = [a+b, a+c, a+d, a+e, b+c, b+d, b+e, c+d, c+e, d+e, e+d, e+c, e+b, e+a, d+c, d+b, d+a, c+b, c+a, b+a]
                    flag = 1
                    for i in temp:
                        if i not in big_list_of_primes:
                            flag = 0
                    if flag == 1:
                        sum = int(a)+int(b)+int(c)+int(d)+int(e)
                        print(f'sum of {a}, {b}, {c}, {d}, {e} is {sum}')
                        print("--- %s seconds ---" % (time.time() - start_time))

print("--- %s seconds ---" % (time.time() - start_time))
# input()