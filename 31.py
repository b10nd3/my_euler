"""
In England the currency is made up of pound, ?, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, ?1 (100p) and ?2 (200p).
It is possible to make ?2 in the following way:

1??1 + 1?50p + 2?20p + 1?5p + 1?2p + 3?1p
How many different ways can ?2 be made using any number of coins?
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