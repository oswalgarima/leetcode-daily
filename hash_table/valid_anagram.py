"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example:
Input: s = "anagram", t = "nagaram"
Output: true
"""


# Runtime: 52ms (52.32%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter

        return Counter(s) == Counter(t)
