def count_islands(grid):
    """grid is a list of strings: '1' is land, '0' is water.
    Land cells that touch up, down, left or right belong to the same island."""
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                count += 1
                flood_fill(grid, visited, r, c)
    return count


def flood_fill(grid, visited, start_r, start_c):
    """DFS with a stack (a recursive version can hit Python's recursion limit)."""
    rows = len(grid)
    cols = len(grid[0])
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True
    while stack:
        r, c = stack.pop()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "1" and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
