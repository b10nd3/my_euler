"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time
start_time = time.time()

summa = 0
# f = open('d:\coding\Python\Euler\p023_numbers.txt', 'w')
#
# list_of_abundant_numbers = []
# def find_all_divisors(x):
#     list_of_divisors = []
#     for i in range(1,x):
#         if x % i ==0:
#             list_of_divisors.append(i)
#     return list_of_divisors
# for x in range(283):
# for x in range(28123):
#     if sum(find_all_divisors(x)) > x:
#         count += 1
#         list_of_abundant_numbers.append(x)
# print(count)
# f.write(str(list_of_abundant_numbers))
# f.close()


with open('d:\coding\Python\Euler\p023_numbers.txt') as f:
    numbers = f.readline()
f.close()


numbers = numbers.split(", ")
for x in range(0, len(numbers)):
    numbers[x] = int(numbers[x])


for x in range(0, 28123):
    flag = 1
    for y in numbers:
        temp = x-y
        if temp < 0:
            break
        if temp in numbers:
            flag = 0
    if flag == 1:
        summa += x
        # print(x)
    if x % 100 == 1:
        print(x)
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
print(summa)


print("--- %s seconds ---" % (time.time() - start_time))
# input()