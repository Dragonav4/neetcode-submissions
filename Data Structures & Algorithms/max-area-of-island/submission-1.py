class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area

        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                max_area = max(max_area, area)
        return max_area
