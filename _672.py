"""
Consider the following process that can be applied recursively to any positive integer n:

if n=1 do nothing and the process stops,
if n is divisible by 7 divide it by 7,
otherwise add 1.
Define g(n) to be the number of 1's that must be added before the process ends. For example:

125-?+1126-??718-?+119-?+120-?+121-??73-?+14-?+15-?+16-?+17-??71.
Eight 1's are added so g(125)=8. Similarly g(1000)=9 and g(10000)=21.

Define S(N)=?Nn=1g(n) and H(K)=S(7K-111). You are given H(10)=690409338.

Find H(109) modulo 1117117717.
"""
for y in range (2, 131):
    count = 0
    x = y
    while True:
        if x % 7 == 0:
            x = x / 7
        else:
            x = x + 1
            count += 1
        if int(x) == 1:
            print(y, count)
            break

