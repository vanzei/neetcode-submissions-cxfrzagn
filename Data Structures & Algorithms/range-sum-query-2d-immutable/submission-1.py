class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumPM = [[0] * (COLS + 1) for j in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range (COLS):
                prefix += matrix[r][c]
                above = self.sumPM[r][c+1]
                self.sumPM[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1 + 1, col1 + 1, row2+1,col2+1
        btRg = self.sumPM[r2][c2]
        tpRg = self.sumPM[r1 - 1][c2]
        btLf = self.sumPM[r2][c1 - 1]
        tpLf = self.sumPM[r1 - 1][c1 - 1]

        return btRg - btLf + tpLf - tpRg 

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)