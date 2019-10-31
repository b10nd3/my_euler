"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import time
start_time = time.time()

big_list_of_primes = []
small_list_of_primes = ['3', '7']
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num
for x in range(8, 1000):
    if is_prime(x):
        small_list_of_primes.append(str(x))
for x in range(2, 1000000):
    if is_prime(x):
        big_list_of_primes.append(str(x))

# small_list_of_primes = ['3', '7', '109', '673', '11']

print("List of Primes is completed")
print(small_list_of_primes)

for a in small_list_of_primes:
    for b in small_list_of_primes:
        if a+b not in big_list_of_primes and b+a not in big_list_of_primes:
            break
        for c in small_list_of_primes:
            if b+c not in big_list_of_primes and c+b not in big_list_of_primes and a+c not in big_list_of_primes and c+a not in big_list_of_primes:
                break
            for d in small_list_of_primes:

                # temp = [a+b, b+a, a+c, c+a, a+d, d+a, b+c, c+b, b+d, d+b, c+d, d+c]
                # # print(temp)
                # flag = 1
                # for i in temp:
                #     if i not in big_list_of_primes:
                #         flag = 0
                # if flag == 1:
                #     print(temp, a, b, c, d)
                #     sum = int(a)+int(b)+int(c)+int(d)
                #     print(f'sum is {sum}')

                if c+d not in big_list_of_primes and d+c not in big_list_of_primes and a+d not in big_list_of_primes and d+a not in big_list_of_primes and b+d not in big_list_of_primes and d+b not in big_list_of_primes:
                    break
                for e in small_list_of_primes:
                    if e + d not in big_list_of_primes and d + e not in big_list_of_primes:
                        break
                    temp = [a+b, b+a, a+c, c+a, a+d, d+a, a+e, e+a, b+c, c+b, b+d, d+b, b+e, e+b, c+d, d+c, c+e, e+c, d+e, e+d]
                    print(a, b, c, d, e, temp)
                    flag = 1
                    for i in temp:
                        if i not in big_list_of_primes:
                            flag = 0
                    if flag == 1:
                        print(a,b,c,d,e,temp)
                        print(int(a)+int(b)+int(c)+int(d)+int(e))


print("--- %s seconds ---" % (time.time() - start_time))
# input()