"""
169. Majority Element
https://leetcode.com/problems/majority-element/


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3
"""


# Runtime: 172ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Thought Process:
        # 1. Using a hash map (dict), to keep the count of each distinct element in the list
        # 2. We filter the dict to find the single element who is the majority
        # 3. Assuming the filtering is guaranteed one elemement being the majority,
        # 4. This means that the the filter dict will likely return only 1 value

        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        return list(dict(filter(lambda val: val[1] > (len(nums) / 2), hash_map.items())))[0]
