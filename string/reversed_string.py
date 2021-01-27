"""
344. Reverse String
https://leetcode.com/problems/reverse-string/


Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


# Runtime: 204ms
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Using a two-pointer solution, where if both pointer == each other, or the front > back
        # We have swap the entire arr around alr

        front_pointer = 0
        back_pointer = len(s) - 1

        while front_pointer < back_pointer:
            # Swapping the front and back
            temp = s[back_pointer]
            s[back_pointer] = s[front_pointer]
            s[front_pointer] = temp

            front_pointer += 1
            back_pointer -= 1
