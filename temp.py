import time
import math
import decimal
start_time = time.time()
sum = 0
count = 0

d2 = decimal.Decimal(223545)
dot100 = decimal.Context(prec=100)
temp = d2.sqrt(dot100)
print(temp)
