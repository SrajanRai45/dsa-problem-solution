def findNonMinOrMax( nums: List[int]) -> int:
    if len(nums) == 2 or len(nums) == 1:
        return -1
    minimum = min(nums)
    maximum = max(nums)
    for i in nums:
        if i != minimum and i != maximum:
            return i
    return -1

nums = [1,2,3,9,6,5]

print(f"{findNonMinOrMax(nums)}")

