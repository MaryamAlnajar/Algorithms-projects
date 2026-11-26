import random
import time
from heap import MaxHeap

# Example from the lecture
heap = MaxHeap()
for name, priority in [("A", 3), ("B", 9), ("C", 5), ("D", 7)]:
    heap.insert(priority, name)
order = []
while len(heap) > 0:
    order.append(heap.extract_max()[1])
print("Lecture example run order:", order)

# 20 random tasks
heap = MaxHeap()
for i in range(20):
    heap.insert(random.randint(1, 100), "task" + str(i))
print("\n20 random tasks, most urgent first:")
while len(heap) > 0:
    priority, name = heap.extract_max()
    print(f"  {name} (priority {priority})")

# Compare with a sorted list that is re-sorted after every insert
print("\nTime for n inserts + n extracts:")
for n in [1000, 2000, 4000, 8000]:
    priorities = [random.randint(1, 1000000) for _ in range(n)]

    start = time.time()
    heap = MaxHeap()
    for i, p in enumerate(priorities):
        heap.insert(p, i)
    for _ in range(n):
        heap.extract_max()
    heap_time = time.time() - start

    start = time.time()
    tasks = []
    for i, p in enumerate(priorities):
        tasks.append((p, i))
        tasks.sort()
    for _ in range(n):
        tasks.pop()
    list_time = time.time() - start

    print(f"n={n:5}  heap={heap_time:.4f}s  sorted list={list_time:.4f}s")
