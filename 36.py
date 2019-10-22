"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time
start_time = time.time()

sum = 0
for x in range(1, 1000001):
    str1 = str(x)
    if str1[::-1] == str1:
        str1 = str("{0:b}".format(x))
        if str1[::-1] == str1:
            print(x, "{0:b}".format(x))
            sum += x

print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
# input()