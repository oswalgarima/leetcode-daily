"""
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/

Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items
in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


Example:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

# Runtime: 52ms


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # Thought process:
        # 1. We need to find the difference between arr1 and arr2

        diff = set(arr1) - set(arr2)

        add_items = sorted([item for item in arr1 if item in diff], reverse=False)
        sort_arr = []

        for i in arr2:
            for j in arr1:
                if j == i:
                    sort_arr.append(i)

        return sort_arr + add_items
