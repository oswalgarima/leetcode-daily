"""
1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/


Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
"""


# Runtime: 32ms
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        sorted_words = sorted(words, key=len)

        sub = []

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if sorted_words[i] in sorted_words[j]:
                    sub.append(sorted_words[i])

        return list(set(sub))
