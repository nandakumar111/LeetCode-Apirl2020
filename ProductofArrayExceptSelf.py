"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        product = 1
        product_of_non_zero = 1
        answer = [0 for i in range(len(nums))]
        count_zero = 0
        for i in nums:
            product *= i
            if i == 0:
                count_zero += 1
            else:
                product_of_non_zero *= i
        for i in range(len(nums)):
            if product != 0:
                answer[i] = product // nums[i]
            elif count_zero == 1:
                if i == 0:
                    answer[i] = product_of_non_zero
        return answer


s = Solution()
print(s.productExceptSelf([1,2,3,4]))
