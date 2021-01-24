"""
1486. XOR Operation in an Array
https://leetcode.com/problems/xor-operation-in-an-array/

Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

Example:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
"""


# Runtime: 28ms
class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        val = 0

        for i in range(start, start + 2 * n, 2):
            val = val ^ i

        return val
