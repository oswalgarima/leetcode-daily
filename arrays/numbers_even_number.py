"""
1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Given an array nums of integers, return how many of them contain an even number of digits.

Example:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
"""


# Runtime: 56ms
class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # Though process:
        # We need to find the length of each number within the array to check for even
        # We can use boolean to help us count the number of True events -> len(i) == even

        return sum([len(str(i)) % 2 == 0 for i in nums])
