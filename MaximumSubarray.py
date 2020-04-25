"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Follow up: If you have
    figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more
    subtle.
"""

def max_crossing_sub_array(arr, low, mid, high):
    left_sum = -1000000
    sum_ele = 0

    for i in range(mid, low - 1, -1):
        sum_ele = sum_ele + arr[i]
        if sum_ele > left_sum:
            left_sum = sum_ele

    right_sum = -1000000
    sum_ele = 0

    for i in range(mid + 1, high + 1):
        sum_ele = sum_ele + arr[i]
        if sum_ele > right_sum:
            right_sum = sum_ele

    return left_sum + right_sum


class Solution:

    def max_sum_sub_array(self, arr, low, high):
        if high == low:
            return arr[high]

        mid = (high + low) // 2

        maximum_sum_left_sub_array = self.max_sum_sub_array(arr, low, mid)
        maximum_sum_right_sub_array = self.max_sum_sub_array(arr, mid + 1, high)
        maximum_sum_crossing_sub_array = max_crossing_sub_array(arr, low, mid, high)

        return max(maximum_sum_left_sub_array, maximum_sum_right_sub_array, maximum_sum_crossing_sub_array)

    def maxSubArray(self, nums) -> int:
        return self.max_sum_sub_array(nums, 0, len(nums) - 1)
