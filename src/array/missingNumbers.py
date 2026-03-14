from collections import Counter

def missingNumber(nums: List[int]) -> int:
    freq = Counter(nums)
    for i in range(0, len(nums)):
        if freq.get(i) == None:
            return i 
    return len(nums)



print(f"in between {missingNumber([0,1,2,3,5])}")
print(f"edge case last element {missingNumber([0,1,2])}")

