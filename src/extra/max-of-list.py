def maximum(nums):
    val = nums[0]
    for i in nums:
        if val < i:
            val = i
    return val


nums = [float("-inf")]
while True:
    carray = int(input("input the next element: "))
    nums.append(carray)
    print("\nAdd more elements?\n[Y or y] for yes or else for no: ", end="")
    temp = input()
    print()
    if temp not in ["y", "Y"]:
        break
print(f"this is the maximum element: {maximum(nums)}")
