class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 1
        for f in range(1,len(nums)):
            if nums[s-1] < nums[f]:
                nums[s] , nums[f] = nums[f] , nums[s]
                s += 1
        return s


