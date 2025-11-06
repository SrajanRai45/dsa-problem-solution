def maxsubarray(self,nums):
    ans = f = nums[0]
    for i in nums[1:]
        f = max(f,0) + i
        ans = max(ans,f)
    return ans

