"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
"""

# Runtime: 20ms (99.04%)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        final_s = ''
        final_t = ''


        for i in S:
            if i != '#':
                final_s += i
            else:
                try:
                    final_s = final_s[:-1]
                except:
                    final_s = ''

        for j in T:
            if j != '#':
                final_t += j
            else:
                try:
                    final_t = final_t[:-1]
                except:
                    final_t = ''

        return final_s == final_t
