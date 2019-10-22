"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import time
start_time = time.time()


for number in range(10, 1000000):
    temp = list(str(number))
    if sorted(list(str(number*2))) == sorted(temp) == sorted(list(str(number*3))) == sorted(list(str(number*4))) == sorted(list(str(number*5))) == sorted(list(str(number*6))):
        print(number, number*2)

print("--- %s seconds ---" % (time.time() - start_time))
# input()