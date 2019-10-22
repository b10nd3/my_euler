"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

y = 600851475143

def is_prime(num):
   d = 2
   while d * d <= num and num % d != 0:
       d += 1
   return d * d > num

for x in range(2, y):
    if y % x == 0:
        delit = int(y / x)
        if is_prime(delit):
            print(delit)
print("calculation ended")