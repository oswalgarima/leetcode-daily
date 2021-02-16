"""
1394. Find Lucky Integer in an Array
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Example:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
"""


# Runtime: 52ms (91.66%)
class Solution:
    def findLucky(self, arr: List[int]) -> int:

        from collections import Counter

        # filter for valid lucky integers
        valid = list(filter(lambda x: x[0] == x[1], Counter(arr).items()))

        # if no lucky integer
        if len(valid) == 0:
            return -1
        else:
            # else sort and return the max
            valid_sort = sorted(valid, key=lambda x: x[0], reverse=True)
            return valid_sort[0][0]
