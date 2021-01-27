"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/


Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not,
return the index where it would be if it were inserted in order.


Example:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""


# Runtime: 52ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Thought process:
        # We just need to add the target into the list
        # Then we sort the list in ascending order
        # Then we return the first occurence of the target in the sorted arr

        nums.append(target)

        return sorted(nums).index(target)
