# Task Scheduler with a Max-Heap

Mini project for CS314, lecture 3 (heaps).

A scheduler that always runs the most urgent task first. The max-heap is written by hand
(a list with `insert` and `extract_max`), no `heapq`.

## How to run

```
python main.py
python test_heap.py
```

`main.py` runs the lecture example (A=3, B=9, C=5, D=7 gives B, D, C, A), then 20 random tasks,
then compares the heap with a list that is sorted again after every insert.
No libraries are needed.

## Results

| n tasks | heap | sorted list |
|---|---|---|
| 1,000 | 0.002 s | 0.006 s |
| 4,000 | 0.010 s | 0.085 s |
| 8,000 | 0.019 s | 0.366 s |

## Notes

- `insert` and `extract_max` each take O(log n), so n tasks cost O(n log n) in total.
- Sorting the list after every insert costs O(n) or more per insert, so it grows like n².
  When n doubles the list time goes up about 4 times, and the heap time about 2 times.
- If two tasks have the same priority, the one whose name is larger comes out first
  (tuples are compared). A simple extension would be to add arrival time.
