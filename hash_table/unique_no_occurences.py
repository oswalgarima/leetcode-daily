"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr,
write a function that returns true if and
only if the number of occurrences of each value in the array is unique.

Example:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false
"""


# Runtime: 24ms (68.14%)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        from collections import Counter

        arr_count = Counter(arr)

        return len(set(arr_count.values())) == len(set(arr))
