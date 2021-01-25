"""
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m x n matrix grid which is sorted in non-increasing order
both row-wise and column-wise,
return the number of negative numbers in grid.

Example:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""


# Thought Process:
# 1. We can either create another array and append the neg value, and count afterwards
# 2. Or we can keep a counter and increase the count whenever we encounter a negative value


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count_neg = 0

        for i in grid:
            for j in i:
                if j < 0:
                    count_neg += 1

        return count_neg

        # for one liner
        # return len([num for element in grid for num in element if num < 0])
