"""
1528. Shuffle String
https://leetcode.com/problems/shuffle-string/

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves
to indices[i] in the shuffled string.

Return the shuffled string.

Example:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""


# Runtime: 68ms
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        # turn the string into indivdiual letters
        letters = [letter for letter in s]
        # zip and sort the based on the indices
        sort_letters = sorted(zip(letters, indices), key=lambda x: x[1], reverse=False)

        return ''.join([pair[0] for pair in sort_letters])
