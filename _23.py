"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time
start_time = time.time()

count = 0
num = 0
int_is_sum_of_abundant_numbers = []
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

# my_set = set(numbers)
# print(numbers)
# print(my_set)

def my_func(numbers, z):
    for index, item in enumerate(numbers):
        if item > z:
            return index, item

for z in range(1, 281):
# for z in range(1, 28124):
    a, b = my_func(numbers, z)
    for x in range(1, a+2):
        for y in range(1, a):
            num = numbers[x]+ numbers[y]
            print(z, x, y, int_is_sum_of_abundant_numbers)
            if not num in int_is_sum_of_abundant_numbers:
                int_is_sum_of_abundant_numbers.append(z)

print(sum(int_is_sum_of_abundant_numbers))



print("--- %s seconds ---" % (time.time() - start_time))
# input()