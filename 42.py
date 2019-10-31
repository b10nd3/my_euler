"""
The nth term of the sequence of triangle numbers is given by, tn = ?n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import time
start_time = time.time()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)
triangle_number = []
count = 0


with open('d:\coding\Python\Euler\p042_words.txt') as f:
    names = f.readline()
f.close()

for n in range(1, 100):
    n = int(n/2*(n+1))
    triangle_number.append(n)

def count_letter_number(word):
    x = list(word)
    word_number = []
    for x in x:
        word_number.append(alphabet.index(x))
    return sum(word_number)


names = names.replace('\",\"', ' ')
names = names.replace('\"', '')
names = sorted(names.split())
names.insert(0, " ")

print(triangle_number)
for x in names:
    print(x)
    if count_letter_number(x) in triangle_number:
        count += 1
print(count)

print("--- %s seconds ---" % (time.time() - start_time))
# input()