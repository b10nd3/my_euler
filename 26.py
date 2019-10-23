"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import time
import math
import decimal
import collections
start_time = time.time()

max_number = 0
max_lenth = 0
x = 0
count = 0

for ch in range(1, 1000):
    ch = decimal.Decimal(ch)
    decimal.getcontext().prec = 3900
    temp = 1/ch

    temp  = str(temp)
    temp = temp[22:3899]

    print(ch, temp)
    for x in range (1, len(temp)):
        if temp[0:x] == temp[x:x+x]:
            count = len(temp[0:x])
            print(temp[0:x])
            break

    if max_lenth < count:
        max_lenth = count
        max_number = ch
print(max_number, max_lenth)


print("--- %s seconds ---" % (time.time() - start_time))
# input()