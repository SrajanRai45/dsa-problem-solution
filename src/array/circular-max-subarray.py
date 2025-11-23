def maxSubarraySumCircular(nums: List[int]) -> int:
    max_sum = neg_max_sum = current_sum = neg_current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        neg_current_sum = min(neg_current_sum + num, num)
        max_sum = max(max_sum, current_sum)
        neg_max_sum = min(neg_current_sum, neg_max_sum)
    circular_result = sum(nums) - neg_max_sum
    if max_sum < 0:
        return max_sum  # edge case // from test case 3 all negative numbers
    return max(circular_result, max_sum)


arr = [-1, -2, -3, 6, 4, -5, -7, 9]
print(f"this is the result {maxSubarraySumCircular(arr)}")
