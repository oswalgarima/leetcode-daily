"""
367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/


Given a positive integer num,
write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example:
Input: num = 16
Output: true
"""

# Runtime: 20ms


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Thought Process
        # ** 0.5 -> returns the sqrt root of an number
        # floor_div returns lowered or actual whole number when dividing
        # excluding the decimal. (e.g., 2.5 -> 2, 3 -> 3)
        floor_div = num // (num ** 0.5)

        # Hence, if a number is perfect square, the num // its square root -> returns a square root
        # Hence if the val squared == original num, it is a perfect square
        return (floor_div * floor_div) == numa
