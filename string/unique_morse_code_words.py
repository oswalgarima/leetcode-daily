"""
804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.


Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""


# Runtime: 80ms (5.15)%
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        # Thought Process:
        # 1. Bruteforce method, zip and dict the mapping of alphabet and morse code
        # 2. for each letter in each word, we replace them and append to an output arr
        # 3. Then set() to remove duplicates and count total amount

        alphabets = [i for i in 'abcdefghijklmnopqrstuvwxyz']

        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                "....", "..", ".---", "-.-", ".-..", "--", "-.",
                "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                "...-", ".--", "-..-", "-.--", "--.."]

        alpha_codes = dict(zip(alphabets, code))

        arr = []

        for word in words:

            word = [i for i in word]

            for i, j in enumerate(word):
                word[i] = alpha_codes.get(j)

            arr.append(''.join(word))

        return len(set(arr))
