"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""
import time
start_time = time.time()

import math

for M in range(98, 105):
    count = 0
    storoni = []
    for a in range(1, M):
        for b in range(1, M):
            for c in range(1, M):
                if math.sqrt((a ** 2 + (b + c) ** 2)).is_integer():
                    if math.sqrt((a**2 + (b+c)**2)) <= math.sqrt((b**2 + (a+c)**2)) and math.sqrt((a**2 + (b+c)**2)) <= math.sqrt((c**2 + (a+b)**2)):
                        temp = [a, b, c]
                        if sorted(temp) not in storoni:
                            storoni.append(sorted(temp))
                            count += 1
    print(M-1, count, count/(M-1))

print("--- %s seconds ---" % (time.time() - start_time))
# input()