"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import time
import math
import itertools
start_time = time.time()

new = list(str(345**3))
print(new)
newlist = list(itertools.permutations(new, 8))
# print(len(newlist))
for x in newlist:
    if (int(''.join(x))**(1/3)).is_integer():
        print(int(''.join(x))**(1/3), int(''.join(x)))

print("--- %s seconds ---" % (time.time() - start_time))







