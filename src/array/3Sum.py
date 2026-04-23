class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        
        for i in range(len(nums)):
            # KEY 1: If this 'i' is the same as the last 'i', skip it.
            # (We use i > 0 so we don't get an IndexError on the very first loop)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum == 0:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # KEY 2: We found a match, so we moved 'l' forward. 
                    # If the new 'l' is the same as the old one, keep moving it.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                elif sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                    
        return results
