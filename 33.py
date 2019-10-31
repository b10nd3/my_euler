"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import time
start_time = time.time()

sumx = 1
sumy = 1
for x in range(10, 100):
    for y in range(10, 100):
        tempx = list(str(x))
        tempy = list(str(y))
        if tempx[1:] == tempy[:1]:
            if int(''.join(tempy[1:])) != 0 and tempx[1:] != tempx[:1]:
                if int(''.join(tempx[:1])) / int(''.join(tempy[1:])) == x / y:
                    print(x, y)
                    sumx *= x
                    sumy *= y
print(f'So we have {sumx}/{sumy}, let\'s try to reduce it;)')

print("--- %s seconds ---" % (time.time() - start_time))
# input()