"""
1464. Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Given the array of integers nums,
you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example:
Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""


# Runtime: 44ms
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Thought proces:
        # We need to take note of the index that generated that highest maximum product of two elements in an array

        #         max_prod = 0

        #         # Given that we must start from 0
        #         for i in range(0, len(nums) - 1):
        #             for j in range(i + 1, len(nums)):
        #                 temp_prod = (nums[i] - 1) * (nums[j] - 1)
        #                 if temp_prod > max_prod:
        #                     max_prod = temp_prod
        #                 else:
        #                     continue

        # Given a more efficient way – the last two number will of a sorted array will always give the bigger prod
        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)
