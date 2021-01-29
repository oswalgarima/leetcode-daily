"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Given a string S of lowercase letters, a duplicate removal consists of
choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.
It is guaranteed the answer is unique.

Example:
Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
 The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""


# Runtime: 84ms
class Solution:
    def removeDuplicates(self, S: str) -> str:

        stack = []

        for i in S:
            # if the current stack is empty, we can just `push` one 1 letter first
            if len(stack) == 0:
                stack.append(i)
            # if the top of the stack is the same as the current letter, we need to `pop` the letter off
            else:
                if i == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)

        return ''.join(stack)
