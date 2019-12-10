"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
import time
start_time = time.time()

with open('d:\coding\Python\Euler\p079_keylog.txt') as f:
    # names = f.readlines()
    names = f.read().split()
f.close()

print(names)
print(final)
for x in names:
    print(x[0], x[1], x[2])
    if x[0] not in final:
        final.insert(0, x[0])
    if x[1] not in final:
        final.insert(5, x[1])
    if x[2] not in final:
        final.insert(8, x[2])

#     if x[0] in final:
#         if final.index(x[0]) != final[5]:
#         if int(x[1]) > final[5]:
# m = '2'
# if m in final:
#     print(final.index(m))
# print(final)
# print(final.index('8'))
# final.insert(final.index('8')+1, '3')
# final.insert(final.index('8'), '2')
# print(final)
# print(final.index('3'))

# 73162890


print("--- %s seconds ---" % (time.time() - start_time))
# input()