"""
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain,
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Example:
Input: arr = [0,1,0]
Output: 1

Input: arr = [3,4,5,1]
Output: 2
"""


# Runtime: 80ms (32.36%)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Though process:
        # Using binary search to find the position of the peak

        # if len(arr) -> given array is a guaranteed mountain array
        # the middle value will be the peak
        if len(arr) == 3:
            return arr[1]

        # initialize the start and end to find the mid
        start, end = 0, len(arr) - 1

        # as long as the start | end does not cross over
        while start <= end:
            # we split the array and find the middle value
            mid = (start + end) // 2
            # given mountain array the left and right value will be smaller than the peak
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            # else if the the right side is bigger, we shift the search to the right ->
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
            # otherwise, we shift it to the left <-
            else:
                end = mid - 1
