import random
import time
from islands import count_islands

grid = [
    "11000",
    "11000",
    "00100",
    "00011",
]
print("Grid:")
for row in grid:
    print(" ", row)
print("Islands:", count_islands(grid))

print("\nRandom grids (about 40% land):")
for size in [100, 200, 400, 800]:
    big = []
    for _ in range(size):
        big.append("".join("1" if random.random() < 0.4 else "0" for _ in range(size)))
    start = time.time()
    islands = count_islands(big)
    elapsed = time.time() - start
    print(f"{size}x{size}: {islands} islands, {elapsed:.3f}s")
