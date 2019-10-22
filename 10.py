"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


num, sum = 2, 0
while num < 2000000:
    if is_prime(num):
        sum += num
        # print(sum, num)
    num += 1
print(sum)
