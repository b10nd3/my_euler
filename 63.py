"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import time
start_time = time.time()

import math

count = 0
# def nth_root(num,root):
#    answer = num ** (1/root)
#    return answer
#
# for x in range(1, 100000000000):
#     root = (len(str(x)))
#     temproot = nth_root(x, root)
#     if round(temproot, 14) == int(temproot):
#         print(x, temproot, root)
#         count += 1

for x in range(1, 100):
    for y in range(1,100):
        if len(str(x**y)) == y:
            count += 1

print(count)
print("--- %s seconds ---" % (time.time() - start_time))
# input()