"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ? 1000, is the number of solutions maximised?
"""
import time
start_time = time.time()


max_var = 0

# p = 1001
p = 180
perim = 0

for p in range(3, 1001):
    list_of_triangles = []
    count = 0
    for a in range(1, p+1):
        for b in range(1, p-a+1):
            for c in range(1, p-a-b+1):
                if a**2+b**2 == c**2 and a+b+c==p:
                    temp = [a, b, c]
                    temp = sorted(temp)
                    if not temp in list_of_triangles:
                        list_of_triangles.append(temp)
                        count = len(list_of_triangles)
    if  max_var < count:
        max_var = count
        perim = p
        print(perim, len(list_of_triangles), list_of_triangles)

print(perim, max_var)
print("--- %s seconds ---" % (time.time() - start_time))
# input()