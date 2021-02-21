"""
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example:
Input: [1,2,2,3]
Output: true

Input: [6,5,4,4]
Output: true
"""

# Runtime: 468ms (70.81%)
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        increasing = sorted(A, reverse=False)
        decreasing = sorted(A, reverse=True)

        return A == increasing or A == decreasing
            
