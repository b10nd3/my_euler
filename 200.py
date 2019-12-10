"""
We shall define a sqube to be a number of the form, p2q3, where p and q are distinct primes.
For example, 200 = 5223 or 120072949 = 232613.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".
"""
import time
start_time = time.time()
import itertools

count = 0
list_of_primes = []
squbelist = []
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num

def is_proof_prime(num):
    flag = 0
    for i in range(0, len(str(num))):
        string = str(num)
        for j in range(0, 10):
            newstring = list(string)
            newstring[i] = str(j)
            if is_prime(int(''.join(newstring))) and int(''.join(newstring)) != 0:
                flag = 1
    if flag == 0:
        return True

for x in range(2, 180000):
    if is_prime(x):
        list_of_primes.append(x)
sqube_primes_list = list(itertools.permutations(list_of_primes, 2))
print("Prime list is generated")
print("--- %s seconds ---" % (time.time() - start_time))

for x in sqube_primes_list:
    if "200" in str(x[0]**2*x[1]**3):
        squbelist.append(x[0]**2*x[1]**3)
squbelist = sorted(squbelist)
print("Squbes list is generated")
print("--- %s seconds ---" % (time.time() - start_time))

for x in squbelist:
    if is_proof_prime(x):
        count += 1
        print(x, "is Prime_Proof", count)
    if count == 200:
        print(x, "200 is FOUND", count)

print("--- %s seconds ---" % (time.time() - start_time))
