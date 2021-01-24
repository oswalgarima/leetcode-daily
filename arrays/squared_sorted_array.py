"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


# Runtime: 200ms
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # i*i is faster than i**2
        # https://stackoverflow.com/questions/51625314/why-vv-is-faster-than-v2-in-python

        nums = [i * i for i in nums]
        nums.sort()

        return nums
