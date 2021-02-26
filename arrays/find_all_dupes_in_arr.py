"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# Runtime: 340ms (89.22%)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        from collections import Counter

        hash_map = Counter(nums)

        return [x[0] for x in list(filter(lambda y: y[1] % 2 == 0, hash_map.items()))]
