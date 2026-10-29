class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            area = 1
            grid[r][c]=0
            while(q):
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r+dr,c+dc
                    if row not in range(rows) or col not in range(cols) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 0
                    q.append((row,col))
                    area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                area = bfs(r,c)
                max_area = max(max_area,area)
        return max_area
                

            