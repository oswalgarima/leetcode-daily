"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.


Example:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""


# Runtime: 60ms (88.27%)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return sorted(nums, reverse=True)[k-1]
