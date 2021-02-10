"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/

You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.


Example:
Input: nums = [1,2,2,4]
Output: [2,3]
"""


# Runtime: 208ms (50.25%)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        from collections import Counter

        orig_nums = set([i for i in range(1, len(nums)+1)])
        dup_nums = list(filter(lambda x: x[1] > 1, Counter(nums).items()))[0][0]

        missing_nums = list(orig_nums - set(nums))[0]

        return [dup_nums, missing_nums]
