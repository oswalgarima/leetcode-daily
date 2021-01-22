'''
1480. Running Sum of 1d Array

Given an array nums. We can define a running sum of an array as runningSum[i] = sum(nums[0],...nums[i])
Return the running sum of nums.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
'''


# Runtime: 36ms
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []

        # for i in range(len(nums)):
        #     num_sum = sum(nums[0:i+1])
        #     lst.append(num_sum)

        # Instead of using list slicing, we can use a temp var
        run_sum = 0
        lst = []

        for i in nums:
            run_sum += i
            lst.append(run_sum)

        return lst
