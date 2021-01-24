"""
561. Array Partition I
https://leetcode.com/problems/array-partition-i/

Given an integer array nums of 2n integers, group these integers into
n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi)
for all i is maximized. Return the maximized sum.

Example:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
"""


# Runtime: 276ms
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # Thought Process:
        # If we want to maximise the sum of minimum value in a pair
        # By sorting them in asc order, each ::2 will always have the maximum
        # value possible in a minimum setting

        nums.sort()

        return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])

        # Faster solution, Runtime: 248ms
        # return sum(sorted(nums)[::2])
