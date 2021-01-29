"""
709. To Lower Case
https://leetcode.com/problems/to-lower-case/


Implement function ToLowerCase() that has a string parameter str,
and returns the same string in lowercase.


Example:
Input: "Hello"
Output: "hello"
"""


# Runtime: 28ms
class Solution:
    def toLowerCase(self, str: str) -> str:

        # Using ASCII method
        return ''.join([chr(ord(i) + 32) if ord(i) >= 65 and ord(i) <= 90 else i for i in str])
