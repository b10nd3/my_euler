"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
       d += 1
    return d * d > num


num, count = 2, 0
while count < 10001:
    if is_prime(num):
        count += 1
        print(count, num)
    num += 1
print(num)
