"""
The following iterative sequence is defined for the set of positive integers:

n ? n/2 (n is even)
n ? 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


max, result = 0, 0
for x in range(3, 1000000):
    count = 1
    y = x
    while y != 1:
        if y % 2 == 0:
            y = y / 2
            count += 1
        else:
            y = y*3 + 1
            count += 1
        if count > max:
            max = count
            result = x
print(result, max)

