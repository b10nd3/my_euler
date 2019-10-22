"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""
import time
start_time = time.time()

sum = 0
max = 0


for a in range(1, 100):
    for b in range(1, 100):
        temp = list(str(a**b))
        for x in temp:
            sum += int(x)
        if max < sum:
            max = sum
        sum = 0
print(max)

print("--- %s seconds ---" % (time.time() - start_time))
# input()