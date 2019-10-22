"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
one_to_nineteen = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
twenty_to_ninety = "twenty thirty forty fifty sixty seventy eighty ninety and hundred"
num_letters = 0

count = []
one_to_nineteen = str.split(one_to_nineteen)
twenty_to_ninety = str.split((twenty_to_ninety))

# print(len(one_to_nineteen), one_to_nineteen)
# print(len(twenty_to_ninety), twenty_to_ninety)


for x in range(0, 1001):
    if x == 1000:
        count.append("one")
        count.append("thousand")
        break
    if x < 20:
        count.append(one_to_nineteen[x])
    if 20 < x < 100:
        count.append(twenty_to_ninety[x // 10 - 2])
        # print(x // 10 - 2)
        if x % 10 != 0:
            count.append(one_to_nineteen[x % 10 - 1])
    if 100 <= x < 1000:
        count.append(one_to_nineteen[x // 100 -1])
        count.append(twenty_to_ninety[9])               # hundred
        if x % 100 != 0:
            count.append(twenty_to_ninety[8])           # and
            if x % 100 <= 20:
                count.append(one_to_nineteen[x % 100-1])
            if x % 100 > 20:
                count.append(twenty_to_ninety[(x % 100) // 10 - 2])
                if x % 10 != 0:
                    count.append(one_to_nineteen[(x % 100) % 10 - 1])


print(len(count), count)
for x in count:
    num_letters += len(x)
print(f'Total {num_letters} letters ')


