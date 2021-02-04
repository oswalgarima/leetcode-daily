"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""


# Runtime: 176ms (27.12%)
class Solution:
    def firstUniqChar(self, s: str) -> int:

        hash_map = {}
        i = 0

        for j in s:
            hash_map[j] = hash_map.get(j, 0) + 1
            i += 1

        unique_chars = list(filter(lambda x: x[1] == 1, hash_map.items()))

        try:
            return s.index(unique_chars[0][0])
        except:
            return -1
