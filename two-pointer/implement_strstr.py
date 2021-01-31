"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Example:
Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input: haystack = "", needle = ""
Output: 0
"""

# Runtime: 32ms


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0
        elif needle in haystack:
            return haystack.find(needle)
        else:
            return -1
