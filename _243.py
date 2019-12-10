"""
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d?1 proper fractions; for example, with d?=?12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d?=?12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""
import time
from fractions import Fraction
start_time = time.time()

nomin = 0
total = 0

# print(15499/94744) # 0.1635881955585578
# print(4/10)        # 0.4

for y in range(2, 17):
# for y in range(170, 27000000, 5000):
    denom = 0
    for x in range(1, y):
        # print(Fraction(x, y))
        if Fraction(x, y).denominator == y:
            denom += 1

    print(denom, "/", (y - 1),"-",Fraction(denom, (y - 1)), denom/(y - 1))

    if Fraction(denom, (y - 1)) < Fraction(15499, 94744):
        print(denom, y-1)





print("--- %s seconds ---" % (time.time() - start_time))
# input()