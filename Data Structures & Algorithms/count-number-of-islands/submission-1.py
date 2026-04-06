class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] != "1":
                return
            
            visited.add((r,c))
            for dr, dc  in directions:
                row, col = r + dr, c + dc

                dfs(row, col)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    dfs(r, c)
        return res                    

            

        