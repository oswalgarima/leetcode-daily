"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


# Runtime: 280ms (14.30%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1
