# Island Counter

Mini project for CS314, graph lecture.

Count the islands in a grid of land (`1`) and water (`0`). Land cells that touch
up, down, left or right are the same island. Diagonals do not count.

A grid is a graph: every land cell is a vertex, and touching land cells are connected by an edge.
Each time I find a land cell I have not seen, I count one island and run DFS to mark the whole island.

## How to run

```
python main.py
python test_islands.py
```

No libraries are needed.

## Example

```
11000
11000
00100
00011
```

Output: 3 islands.

## Results (random grids, 40% land)

| Grid | Islands found | Time |
|---|---|---|
| 100 x 100 | 1,043 | 0.002 s |
| 400 x 400 | 16,841 | 0.040 s |
| 800 x 800 | 68,155 | 0.203 s |

(The island numbers change on every run because the grids are random.)

## Notes

- Time is O(V + E), where V is the number of cells. When the grid went from 400x400 to 800x800
  (4 times more cells) the time went up about 5 times, so it is close to linear.
- I used a stack instead of recursion. A long snake-shaped island would hit Python's recursion limit
  with a recursive DFS.
- Tested: empty grid, all water, all land, a diagonal (two islands), one cell, and a snake shape.
