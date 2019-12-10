"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
import time
start_time = time.time()

count = 0

for p100 in range(0, 3):
    for p50 in range(0, 5):
        for p20 in range(0, 11):
            for p10 in range(0, 21):
                for p5 in range(0, 41):
                    for p2 in range(0, 101):
                        for p1 in range(0, 201):
                            if p100*100+p50*50+p20*20+p10*10+p5*5+p2*2+p1 == 200:
                                # print(p100, p50, p20, p10, p5, p2, p1)
                                count += 1
print(count+1)

print("--- %s seconds ---" % (time.time() - start_time))
# input()