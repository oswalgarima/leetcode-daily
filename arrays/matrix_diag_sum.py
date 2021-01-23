"""
1572. Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal
and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""


# Runtime: 112ms
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        # Though process:
        # Need to check the number of rows/columns in the matrix
        # If odd, the centre value has to be only counted once
        # Cannot use a set cuz the matrix may all be the same number

        sum = 0

        # If odd
        if len(mat) % 2 != 0:
            # Find the middle value if even
            middle_index = int(len(mat) / 2 - .5)
            middle_value = mat[middle_index][middle_index]
            for i in range(len(mat)):
                # Adding primaary diagonal
                sum += mat[i][i]
                # Adding secondary diagonal
                sum += mat[i][-1-i]
            sum -= middle_value
        else:
            for i in range(len(mat)):
                # Adding primary diagonal
                sum += mat[i][i]
                # Adding secondary diagonal
                sum += mat[i][-1-i]

        return sum
