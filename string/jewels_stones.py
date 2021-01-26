"""
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""


# Runtime: 48ms (Both)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # # Getting count for each letter (case-sensitive)
        # jewels_count = {x: jewels.count(x) for x in jewels}
        # stones_count = {y: stones.count(y) for y in stones}
        #
        # # Find the intersection keys and retrieves the relevant dict with intersecting keys
        # intersection = {x:stones_count[x] for x in stones_count if x in jewels_count}
        #
        # return sum(intersection.values())

        # Using list comprehension and if/else instead
        return sum([1 for x in stones if x in jewels])
