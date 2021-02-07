"""
1748. Sum of Unique Elements
https://leetcode.com/problems/sum-of-unique-elements/

You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
"""


# Runtime: 32ms (100%)
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        from collections import Counter

        num_count = Counter(nums)

        return sum(dict(filter(lambda x: x[1] == 1, num_count.items())).keys())
