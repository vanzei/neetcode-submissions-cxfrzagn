class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                bot = mid - 1

        # top is the first row with last >= target (insertion point)
        if top == ROWS:
            return False
        row = top
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False
