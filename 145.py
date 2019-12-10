"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""
import time
start_time = time.time()

count = 0
to = 10**9

for x in range(0, to):
    if str(x)[-1] != "0":
        summa = x + int(str(x)[::-1])
        flag = 0
        for i in str(summa):
            if int(i) % 2 == 0 or i == '0':
                flag = 1
        if flag == 0:
            count += 1
            # print(x, summa)


print(count)

print("--- %s seconds ---" % (time.time() - start_time))
# input()