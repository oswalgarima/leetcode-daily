"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.


Example:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"
"""

# Runtime: 132ms


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # Handling edge case where target >= maximum letter of letters
        if target >= max(letters):
            return min(letters)
        else:
            # Else in normality, we pick the minimum letter among those who are greater than the target
            return min([i for i in letters if i > target])
