"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
sum = 0
for x in range(10000, 99999):
    number = str(x)
    # print(x)
    for y in number:
        sum = 0
        sum = int(number[0]) ** 5 + int(number[1]) ** 5 + int(number[2]) ** 5 + int(number[3]) ** 5 + int(number[4]) ** 5
        if sum == int(x):
            print(x, y, sum)

print(54748 + 92727 + 93084)