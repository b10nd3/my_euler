"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import time
import math
import decimal
start_time = time.time()
sum = 0
count = 0

for ch in range(1, 100):
    d2 = decimal.Decimal(ch)
    dot100 = decimal.Context(prec=110)
    temp = d2.sqrt(dot100)
    if ch % temp != 0:
        count += 1
        temp = list(str(temp))
        # y = temp.index('.')
        # del temp[0:y+1]
        temp = [x for x in temp if x != '.']
        for i in range(100):
            sum += int(temp[i])
        if count == 100:
            print(sum)
print(sum)


print("--- %s seconds ---" % (time.time() - start_time))
# input()