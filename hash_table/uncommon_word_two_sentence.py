"""
884. Uncommon Words from Two Sentence
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Example:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
"""


# Runtime: 32ms (61.57%)
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        from collections import Counter

        sentence = A + ' ' + B

        hash_map = Counter(sentence.split(' '))

        return [x[0] for x in list(filter(lambda x: x[1] == 1, hash_map.items()))]
