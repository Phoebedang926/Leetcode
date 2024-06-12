class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1
        
        while top <= bot:
            mid = (top+bot)//2
            if matrix[mid][0] > target:
                bot = mid -1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if top > bot: return False
        
        l, r = 0, cols -1
        while l <=r:
            m = (l +r)//2
            if matrix[mid][m]> target:
                r = m - 1
            elif matrix[mid][m]< target:
                l = m +1
            else:
                return True
        return False
