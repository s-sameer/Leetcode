'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
# Intuition: We can use BFS to find connected components in the grid.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    if ((row+dr) in range(rows) and
                        (col+dc) in range(cols) and
                        grid[row+dr][col+dc] == "1" and
                        (row+dr, col+dc) not in visit):
                        queue.append((row+dr, col+dc))
                        visit.add((row+dr, col+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands