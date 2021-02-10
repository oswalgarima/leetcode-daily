"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true
"""


# Runtime: 28ms (85.58%)
class Solution:
    def isValid(self, s: str) -> bool:

        left = '({['
        right = ')}]'

        stack = []

        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                # it closes before there's any opening
                if not stack:
                    return False
                if right.index(i) != left.index(stack.pop()):
                    return False

        return not stack
