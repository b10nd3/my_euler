print("""
n! means n ? (n ? 1) ? ... ? 3 ? 2 ? 1

For example, 10! = 10 ? 9 ? ... ? 3 ? 2 ? 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
""")

result = 1
sum = 0
for x in range(1, 101):
    result = result * x
    print(x, result)

print(result)
str = str(result)
print(list(str))
for x in range(0, len(str)):
    sum += int(str[x])
print(sum)