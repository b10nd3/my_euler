"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 ? 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import time
start_time = time.time()


list_of_products = []
pandigital = list("123456789")
max_summa = 0
count = 0
maximum = 0


def is_multidigital(num):
    if sorted(list(str(num))) == pandigital:
        print(num)
        return True
        # return num


for x in range(1, 10000):
    for y in range(1, 1000):
        temp = x * y
        if is_multidigital(str(x)+str(y)+str(temp)):
            print(x, y, temp)
            if temp not in list_of_products:
                list_of_products.append(temp)

print(sum(list_of_products))


print("--- %s seconds ---" % (time.time() - start_time))
# input()