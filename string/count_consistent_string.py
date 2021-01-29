"""
1684. Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/

You are given a string allowed consisting of distinct characters and
an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""


# Runtime: 352ms
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        distinct_letters = [set(word) for word in words]
        # check the difference between set(word) vs set(allowed)
        difference_letters = [word - set(allowed) for word in distinct_letters]

        return sum([1 for i in difference_letters if len(i) == 0])
