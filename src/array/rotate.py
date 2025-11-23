arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rotate(nums: List[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


rotate(arr, 3)
print(arr)
