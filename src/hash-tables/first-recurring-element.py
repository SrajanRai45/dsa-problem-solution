def FindFirstRecurrigElement(nums: List[int]) -> int | None:
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    buffer = -float("inf")
    for i in frequency.keys():
        if frequency[i] > buffer:
            buffer = i
    return None if buffer == -float("inf") else buffer


arr = [1, 2, 3, 4, 5, 1, 3, 4, 1, 3, 5, 6, 8, 4, 3, 5, 6, 3, 3, 5]

print(
    f"this is the answer for the first recurring element for the following array \n{arr} \n solution : {FindFirstRecurrigElement(arr)}"
)
