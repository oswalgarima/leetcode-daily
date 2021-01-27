"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example:
Input: [1,2,3,1]
Output: true
"""

# Runtime: 128ms


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = hash_map.get(0, num,) + 1
            else:
                return True

        return False
