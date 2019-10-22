"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 ? 32 ? 13 ? 10 ? 1 ? 1
85 ? 89 ? 145 ? 42 ? 20 ? 4 ? 16 ? 37 ? 58 ? 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
import time
start_time = time.time()

sum = 0
count = 0

def sum_of_square_digits(a):
    sum = 0
    temp = list(str(a))
    for x in temp:
        sum += int(x)**2
    return sum

for x in range(1, 10000000):
# for x in range(1, 10000):
    while x!=1:
        # print(x)
        x = sum_of_square_digits(x)
        if x == 89:
            count += 1
            break
print(count)

print("--- %s seconds ---" % (time.time() - start_time))
# input()