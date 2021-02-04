"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/


Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.


Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


# Runtime: 100ms (11.40%)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        curr_sum = max_sum

        for i in range(1, len(nums)):
            curr_sum = max(nums[i] + curr_sum, nums[i])
            max_sum = max(curr_sum, max_sum)

        return max_sum
