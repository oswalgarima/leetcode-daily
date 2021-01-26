"""
1502. Can Make Arithmetic Progression From Sequence
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Given an array of numbers arr. A sequence of numbers is called an arithmetic progression
if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.


Example:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1]
with differences 2 and -2 respectively, between each consecutive elements.
"""

# Runtime: 36ms


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        # Thought Process:
        # Arithmetic progression formula: an = a1 + (n - 1)d
        # 2. We need to keep track of the very first sorted difference
        # 3. Using that difference, we compared each sub diff to it
        # 4. If different, = no progression

        # First we need to sort the arr
        arr.sort()
        # Compute the difference using list comprehension
        differences = [arr[i+1] - arr[i] for i in range(len(arr) - 1)]
        if differences.count(differences[0]) != len(differences):
            return False
        else:
            return True
