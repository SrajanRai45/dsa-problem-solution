class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenMatrix = len(matrix)
        lenArr = len(matrix[0])
        col = lenArr -1
        row = 0
        if lenMatrix == 0:
            return False
        elif lenMatrix == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        while col >= 0 and row < lenMatrix:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                #fallback column
                col -= 1
            elif matrix[row][col] < target:
                #increase row
                row += 1
        return False
                
