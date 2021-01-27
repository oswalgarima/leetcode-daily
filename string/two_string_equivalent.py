"""
1662. Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Given two string arrays word1 and word2, return true if the two arrays
epresent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.


Example:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

# Runtime: 32ms


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        return ''.join(word1) == ''.join(word2)
