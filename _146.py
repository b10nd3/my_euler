"""
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""
import time
import math
start_time = time.time()

count = 0
summa = 0
int_is_prime = set()

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

# for x in range(2, 1000000000028):
for x in range(2, 10000):
    if is_prime(x):
        int_is_prime.add(x)
print("--- %s seconds ---" % (time.time() - start_time))
print("Set of Primes is completed")

# f = open('d:\coding\Python\Euler\prime_up_to_10x12.txt', 'w')
# f.write(str(int_is_prime))
# f.close()

# with open('d:\coding\Python\Euler\prime_up_to_10x12.txt') as f:
#     numbers = f.readline()
# f.close()
# numbers = numbers.split(", ")
# for x in range(0, len(numbers)):
#     numbers[x] = int(numbers[x])

# for x in int_is_prime:
#     temp = math.sqrt(x-1)
#     if temp % 1 == 0:
#         temp = int(temp)
#         if temp**2+3 in int_is_prime:
#             if temp**2+7 in int_is_prime:
#                 if temp**2+9 in int_is_prime:
#                     if temp**2+13 in int_is_prime:
#                         if temp**2+27 in int_is_prime:
#                             print(temp)


for n in range(0, 150000000, 10):
    if is_prime(n**2+1):
        if is_prime(n**2+3):
            if is_prime(n**2+7):
                if is_prime(n**2+9):
                    if is_prime(n**2+13):
                        if is_prime(n**2+27):
                            print(n)
                            summa += n
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue



# for n in range(0, 1000000, 10):
#     print(n)
#     if n**2+1 in int_is_prime:
#         if n**2+3 in int_is_prime:
#             if n**2+7 in int_is_prime:
#                 if n**2+9 in int_is_prime:
#                     if n**2+13 in int_is_prime:
#                         if n**2+27 in int_is_prime:
#                             print(n)
#                             summa += n
#                     else:
#                         continue
#                 else:
#                     continue
#             else:
#                 continue
#         else:
#             continue
#     else:
#         continue

print(summa)

# 10**2 = 100
# 315410**2 = 99483468100
# 927070**2 = 859458784900
# 2525870**2 = 6380019256900
# 8146100**2 = 66358945210000

print("--- %s seconds ---" % (time.time() - start_time))
# input()