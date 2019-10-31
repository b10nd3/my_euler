"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 ? 1 = 192
192 ? 2 = 384
192 ? 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
import time
start_time = time.time()


list_of_primes = []
pandigital = list("123456789")
max_summa = 0
count = 0
maximum = 0


def is_multidigital(num):
    if sorted(list(str(num))) == pandigital:
        # return True
        return num


def make_concatenated(number, concatenator):
    chislo = ""
    for x in concatenator:
        chislo += str(number * x)
    return int(chislo)


for x in range(1, 10000):
    for y in range(1, 5):
        temp = make_concatenated(x, [i for i in range(0, y)])
        if is_multidigital(temp):
            print(temp)
            if maximum < int(temp):
                maximum = int(temp)

print(count, maximum)


print("--- %s seconds ---" % (time.time() - start_time))
# input()