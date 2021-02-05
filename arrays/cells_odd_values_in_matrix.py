"""
1252. Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/


Given n and m which are the dimensions of a matrix initialized by zeros and
given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci]
you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after
applying the increment to all indices.


Example:
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
"""


# Runtime: 52ms (43.15%)
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        # creating the matrix
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in indices:
            # row operations
            matrix[i[0]] = [x+1 for x in matrix[i[0]]]
            # columns operations
            for row in matrix:
                row[i[1]] = row[i[1]] + 1

        count = 0
        for row in matrix:
            # counting boolean that satisfy condition
            # https://thispointer.com/python-count-elements-in-a-list-that-satisfy-certain-conditions/
            arr_count = sum(map(lambda x: x % 2 == 1, row))
            count += arr_count

        return count
