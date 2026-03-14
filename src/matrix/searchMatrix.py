class Solution:
    def binSearch(self , nums : List[int] , target : int):
        arrLen = len(nums)
        left = 0
        right = arrLen - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            elif target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
         
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arrLen = len(matrix)
        left = 0
        right = arrLen -1
        while left <= right:
            mid = left + (right - left) // 2
            flag = self.binSearch(matrix[mid],target)
            if flag:
                return flag
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

