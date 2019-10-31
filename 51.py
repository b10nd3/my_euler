"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
import time
start_time = time.time()


int_is_prime = []
def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


for x in range(2, 1000000):
    if is_prime(x):
        int_is_prime.append(x)

def replace_three_digits(x):
    digits = []
    tempx = list(str(x))
    for a in range(0, len(tempx)):
        for b in range(a+1, len(tempx)):
            for c in range(b+1, len(tempx)):
                tempy = tempx.copy()
                digitsi = []
                for i in range(0, 10):
                    tempy[a], tempy[b], tempy[c] = i, i, i
                    digitsi.append(int(''.join((str(i) for i in tempy))))
                digits.append(digitsi)
    return digits

# temp = replace_three_digits(1234567)
# print(len(temp), temp)


for x in int_is_prime:
    temp = replace_three_digits(x)
    # temp = replace_two_digits(x)
    for i in temp:
        temps = []
        for y in i:
            if y in int_is_prime:
                temps.append(y)
        if len(temps) == 8:
            print(x, sorted(temps), i)


print("--- %s seconds ---" % (time.time() - start_time))
# input()