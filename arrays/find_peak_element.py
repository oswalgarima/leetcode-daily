"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/


A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""


# Runtime: 36ms (98.59%)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        peak = sorted(nums, reverse=True)[0]

        return nums.index(peak)
