"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 ? d10 ? d100 ? d1000 ? d10000 ? d100000 ? d1000000
"""
import time
start_time = time.time()
list = []

for number in range(1, 4000000):
    list.append((str(number)))
print(list)
list = ''.join(list)
print(list)
print(int(list[0]) * int(list[9]) * int(list[99]) *  int(list[999]) *  int(list[9999]) *  int(list[99999]) * int(list[999999]))

print("--- %s seconds ---" % (time.time() - start_time))
# input()