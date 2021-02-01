"""
832. Flipping an Image
https://leetcode.com/problems/flipping-an-image/

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].


Example:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""


# Runtime: 64ms (11.45%)
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        # Thought process:
        # First, we need to reversed each element within the array first
        # Using ->  x = 1 - x
        # Then, we invert each individual element with 0/1 accordingly
        # Using arr[::-1]

        temp = []

        for arr in A:
            arr = map(lambda x: (1 - x),  arr)
            temp.append(list(arr)[::-1])

        return temp
