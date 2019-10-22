"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

result = 1

for x in range(1, 41):
    result = result * x
    print(x, result)

print(815915283247897734345611269596115894272000000000/2432902008176640000**2)
