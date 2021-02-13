"""
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""


# Runtime: 328ms (82.02%)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        curr_min = float('inf')
        output = []

        for i in range(0, len(arr)-1):
            # check the curr_min
            temp_min = abs(arr[i+1] - arr[i])
            if temp_min < curr_min:
                curr_min = temp_min
                output = [[arr[i], arr[i+1]]]
            elif temp_min == curr_min:
                output.append([arr[i], arr[i+1]])

        return output
