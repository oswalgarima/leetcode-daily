"""
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/


Given two arrays, write a function to compute their intersection.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""


# Runtime: 44ms
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return set(nums1).intersection(set(nums2))
