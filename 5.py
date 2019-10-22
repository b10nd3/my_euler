"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num, is_good = 1, False
for num in range(0, 1900000000000, 20):
    for i in range(1, 20):
        if num % i == 0:
            is_good = True
        else:
            is_good = False
            break
    if is_good:
        print(num)
    num += 1