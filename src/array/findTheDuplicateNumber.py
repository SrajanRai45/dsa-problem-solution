from collections import Counter

def findDuplicate(nums: List[int]) -> int:
    freq = Counter(nums)
    for i in nums:
        if freq.get(i) >= 2:
            return i

print(findDuplicate([1,2,3,4,2]))

