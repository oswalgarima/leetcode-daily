"""
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/


Example:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
"""


# Runtime; 48ms (88.46%)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        distinct_nums = set(nums)

        if len(distinct_nums) < 3:
            return sorted(distinct_nums, reverse=True)[0]
        else:
            return sorted(distinct_nums, reverse=True)[2]
