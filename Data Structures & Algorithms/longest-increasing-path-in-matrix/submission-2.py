class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevValue):
            if (r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prevValue):
                return 0

            if (r, c) in dp:
                return dp[(r,c)]
            
            res = 1
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dirs in directions:
                row, col = r + dirs[0], c + dirs[1]
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())