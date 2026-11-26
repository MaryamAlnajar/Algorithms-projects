import random
import time
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort, merge_sort

sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
times = {"sorted": [], "reverse": [], "random": []}
merge_times = []

for n in sizes:
    inputs = {
        "sorted": list(range(n)),
        "reverse": list(range(n, 0, -1)),
        "random": [random.randint(0, 10000) for _ in range(n)],
    }
    for name, data in inputs.items():
        start = time.time()
        result, comps, shifts = insertion_sort(data)
        times[name].append(time.time() - start)
        print(f"n={n:5} {name:8} comparisons={comps:9} shifts={shifts:9} time={times[name][-1]:.4f}s")

    start = time.time()
    merge_sort(inputs["random"])
    merge_times.append(time.time() - start)

plt.figure(figsize=(8, 5))
for name in times:
    plt.plot(sizes, times[name], marker="o", label="insertion sort - " + name)
plt.plot(sizes, merge_times, marker="s", linestyle="--", label="merge sort - random")
plt.xlabel("n")
plt.ylabel("time (seconds)")
plt.title("Insertion sort running time")
plt.legend()
plt.grid(True)
plt.savefig("running_time.png", dpi=120)
print("saved running_time.png")
