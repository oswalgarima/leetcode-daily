"""
1550. Three Consecutive Odds
https://leetcode.com/problems/three-consecutive-odds/

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
"""


# Runtime: 48ms
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        # Only take element if element % 2 == 1

        for i in range(len(arr) - 2):
            if sum([1 for i in arr[i: i+3] if i % 2 == 1]) == 3:
                return True

        return False
