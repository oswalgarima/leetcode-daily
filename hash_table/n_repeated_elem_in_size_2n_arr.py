"""
961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.


Example:
Input: [1,2,3,3]
Output: 3
"""

# Runtime: 228ms (28.99%)


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        from collections import Counter

        count = Counter(A)

        n = len(A) / 2

        return list(filter(lambda x: x[1] == n, count.items()))[0][0]
