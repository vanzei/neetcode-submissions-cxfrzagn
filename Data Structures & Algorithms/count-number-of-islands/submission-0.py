class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def dfs (r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in seen or grid[r][c] != "1":
                    return
            seen.add((r,c))
            directions = [(0,1),(1,0),(-1,0),(0,-1)]

            for dr, dc in directions:
                dfs(dr + r, dc + c)
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    islands += 1
                    dfs(r, c)
        return islands


        
        