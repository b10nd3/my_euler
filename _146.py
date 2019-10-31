"""
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""
import time
start_time = time.time()

count = 0
flag = 0
int_is_prime = []
summa = 0

def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

# for x in range(2, 1000000000028):
for x in range(2, 1000000):
    if is_prime(x):
        int_is_prime.append(x)
print("List of Primes is completed")

# print(int_is_prime)
# f = open('d:\coding\Python\Euler\prime_up_to_10x12.txt', 'w')
# f.write(str(int_is_prime))
# f.close()

for x in int_is_prime:
    temp = math.sqrt(x-1)
    if temp % 1 == 0:
        temp = int(temp)
        if temp**2+3 in int_is_prime:
            if temp**2+7 in int_is_prime:
                if temp**2+9 in int_is_prime:
                    if temp**2+13 in int_is_prime:
                        if temp**2+27 in int_is_prime:
                            print(temp)



# with open('d:\coding\Python\Euler\prime_up_to_10x12.txt') as f:
#     numbers = f.readline()
# f.close()
# numbers = numbers.split(", ")
# for x in range(0, len(numbers)):
#     numbers[x] = int(numbers[x])

#
# for n in range(2, 1000000):
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
#
# print(summa)


print("--- %s seconds ---" % (time.time() - start_time))
# input()