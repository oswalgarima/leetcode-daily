"""
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example:
Input: nums = [1,2,3]
Output: 6

Input: nums = [1,2,3,4]
Output: 24
"""

# Runtime: 252ms (73.64%)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()

        incld_neg = 1
        excld_neg = 1

        w_neg_val = nums[:2] + [nums[-1]]
        pos_val = nums[-3:]

        for i in w_neg_val:
            incld_neg *= i

        for j in pos_val:
            excld_neg *= j


        return max(incld_neg, excld_neg)
