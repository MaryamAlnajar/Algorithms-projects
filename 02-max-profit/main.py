import csv
import random
import time
from max_profit import linear_scan, divide_and_conquer

prices = []
with open("prices.csv") as f:
    for row in csv.DictReader(f):
        prices.append(float(row["price"]))

print("Days:", len(prices))
for name, func in [("linear scan", linear_scan), ("divide and conquer", divide_and_conquer)]:
    profit, buy, sell = func(prices)
    print(f"{name}: profit={profit:.2f}, buy on day {buy + 1}, sell on day {sell + 1}")

print()
print("Timing on bigger random price lists:")
for n in [1000, 10000, 100000, 500000]:
    data = [100]
    for i in range(n - 1):
        data.append(data[-1] + random.uniform(-3, 3))
    start = time.time()
    linear_scan(data)
    t1 = time.time() - start
    start = time.time()
    divide_and_conquer(data)
    t2 = time.time() - start
    print(f"n={n:7}  linear={t1:.4f}s  divide&conquer={t2:.4f}s")
