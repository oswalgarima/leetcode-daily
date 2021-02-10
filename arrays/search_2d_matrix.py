"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


# Runtime: 44ms (65.40%)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Thought process:
        # you only need to look at start value and find the last index of which where the target is < that start val
        # hence you lower the search area, and you can start to search in that matrix[index]

        start_val = [arr[0] for arr in matrix]

        start_pos = 0

        for idx, val in enumerate(start_val):
            if val <= target:
                start_pos = idx

        return target in matrix[start_pos]
