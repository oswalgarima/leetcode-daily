"""
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/


You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.


Example:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""


# Runtime: 40ms
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        first, second = s[:int(len(s) / 2)], s[int(len(s) / 2):]

        first_count, second_count = 0, 0

        for letter in first:
            if letter in vowels:
                first_count += 1

        for letter in second:
            if letter in vowels:
                second_count += 1

        return first_count == second_count
