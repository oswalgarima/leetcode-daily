"""
1720. Decode XORed Array
https://leetcode.com/problems/decode-xored-array/

There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1,
such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.


Example:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
"""


# Runtime: 232ms
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        # The first element in the hidden array: first
        arr = [first]
        # Initialise a temp variable to keep track of each reverse XOR
        temp = 0

        for idx, val in enumerate(encoded):
            # a ^ b = c -> b = a ^ c
            # to reverse an encoded XORed array, we need to XOR either value resulting in the XORed value
            # the first element in the encoded array must XOR the first element in the hidden array
            if idx == 0:
                temp = first ^ val
            # subsequently, we can just use the temp variable which to slowly decode the arr
            else:
                temp ^= val

            arr.append(temp)

        return arr
