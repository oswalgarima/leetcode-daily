"""
1619. Mean of Array After Removing Some Elements
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

Given an integer array arr, return the mean of the remaining integers
after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.

Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum values of this array,
all elements are equal to 2, so the mean is 2.
"""

# Runtime: 68ms


class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()

        five_pct = int(len(arr) / 100 * 5)

        return sum(arr[five_pct: len(arr) - five_pct]) / (len(arr) - five_pct * 2)
