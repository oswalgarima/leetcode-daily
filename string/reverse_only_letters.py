"""
917. Reverse Only Letters
https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters
that are not a letter stay in the same place, and all letters reverse their positions.

Example:
Input: "ab-cd"
Output: "dc-ba"

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
"""


# Runtime: 32ms (64.43%)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        reversed_letters = [i for i in S if i.isalpha()][::-1]

        output = ''
        i = 0

        if len(reversed_letters) == 0:
            return S

        while i < len(reversed_letters):
            for j in S:
                if j.isalpha():
                    output += reversed_letters[i]
                    i += 1
                else:
                    output += j

        return output
