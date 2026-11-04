class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        q = deque()

        def bfs(fresh_oranges):
            minutes = 0
            while q and fresh_oranges > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row, col = dr + r, dc + c
                        if (
                            row not in range(rows)
                            or col not in range(cols)
                            or grid[row][col] != 1
                        ):
                            continue
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh_oranges -= 1
                minutes += 1
            return (minutes, fresh_oranges)

        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        time_spend, fresh_orangs = bfs(fresh_oranges)
        if fresh_orangs > 0: return -1
        return time_spend
