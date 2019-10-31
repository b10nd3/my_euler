import math
N = 1000000000
def p(N):
    s = set(range(1, N, 2))
    for i in range(2, int(math.sqrt(N))):
        if i in s:
            s -= set(range(i*i, N, i))
    return s

#print(p(N))

f = open('d:\coding\Python\Euler\prime_up_to_10x12.txt', 'w')
f.write(str(p(N)))
f.close()