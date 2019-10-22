"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

sum = 0
s = str(2 ** 1000)
s = list(s)
for x in range(0, len(s)):
    sum += int(s[x])
print(sum)