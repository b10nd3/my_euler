"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""
import time
import math
start_time = time.time()

count = 0
top = 10**10
my_array = []

for m in range(2, 100):
    for n in range(2, 10):
        if m**n not in my_array:
            my_array.append(m**n)
my_array = sorted(my_array)

for a in my_array[10:]:
    summa = 0
    for y in str(a):
        summa += int(y)
    for x in range(1, 19):
        if summa**x > a:
            break
        if summa**x == a:
            count += 1
            print(f'� {count}. summa ciphers of  {a} =  {summa} in power of {x}')

print("--- %s seconds ---" % (time.time() - start_time))
# input()

# � 1. summa ciphers of  81 =  9 in power of 2
# � 2. summa ciphers of  512 =  8 in power of 3
# � 3. summa ciphers of  2401 =  7 in power of 4
# � 4. summa ciphers of  4913 =  17 in power of 3
# � 5. summa ciphers of  5832 =  18 in power of 3
# � 6. summa ciphers of  17576 =  26 in power of 3
# � 7. summa ciphers of  19683 =  27 in power of 3
# � 8. summa ciphers of  234256 =  22 in power of 4
# � 9. summa ciphers of  390625 =  25 in power of 4
# � 10. summa ciphers of  614656 =  28 in power of 4
# � 11. summa ciphers of  1679616 =  36 in power of 4
# � 12. summa ciphers of  17210368 =  28 in power of 5
# � 13. summa ciphers of  34012224 =  18 in power of 6
# � 14. summa ciphers of  52521875 =  35 in power of 5
# � 15. summa ciphers of  60466176 =  36 in power of 5
# � 16. summa ciphers of  205962976 =  46 in power of 5
# � 17. summa ciphers of  612220032 =  18 in power of 7
