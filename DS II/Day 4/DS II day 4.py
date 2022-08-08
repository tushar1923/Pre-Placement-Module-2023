class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])-1
        for item in range(len(matrix)):
            while matrix[item][col] > target and col >= 0:
                col-=1
            if matrix[item][col] == target:
                return True
        return False
