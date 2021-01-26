"""
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if
it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1]
holds for every i (0-based) such that (0 <= i <= n - 2).

Example:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
"""


# Runtime: 224ms
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        # Thought Process:
        # 1. There can only be 1 instance where the sequence is non non-decreasing (increasing)
        # 2. Do not need think about the value to be modify since == also counts, hence we can just remove it
        # 3. Since it is supposed to be increasing, after removing the at most 1 error, we can compare existing modified
        # 4. Array with sorted-array

        # If you have less than 3 elements in an array, all you need is 1 modification to get non-decreasing
        if len(nums) <= 2:
            return True
        else:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums.copy()
                    # nums[i] can either be larger than usual in a sequence or
                    temp.pop(i)
                    # nums[i+1] is smaller than usual
                    nums.pop(i+1)
                    # After modifying by removing either the violating large or smaller number in a seq, we can then compared with its sorted version
                    # Since sorted version, will always sort increasing manner
                    return temp == sorted(temp) or nums == sorted(nums)

            # If no instances where non-decreasing is violated, all conditions are True
            return True
