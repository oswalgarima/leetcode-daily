"""
1512. Number of Good Pairs


Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


Example:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""


# Runtime: 28ms


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0

        for i in range(0, len(nums) - 1):
            # exclusive of the last num
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count
