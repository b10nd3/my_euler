"""
# Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x ? y, x + z, x ? z, y + z, y ? z are all perfect squares.
# """
import time
import math
start_time = time.time()

top = 100000

for z in range(1, top):
    for y in range(z+1, top):
        if not math.sqrt(y+z).is_integer() or math.sqrt(y-z).is_integer():
            # print(y,z)
            continue
        for x in range(y+1, top):
            # print(x, y, z)
            if math.sqrt(x+y).is_integer() and math.sqrt(x-y).is_integer() and math.sqrt(x+z).is_integer() and math.sqrt(x-z).is_integer() and math.sqrt(y+z).is_integer() and math.sqrt(y-z).is_integer():
                print(x,y,z, x+y+z)


print("--- %s seconds ---" % (time.time() - start_time))
# input()