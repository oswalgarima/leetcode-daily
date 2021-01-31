"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""


# Runtime: 5868ms
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        # Believes its a very bruteforce method
        # First we loop through every possible value in A
        for idx, val in enumerate(A):
            # We will take note of the next value
            next_val = idx + 1
            # If the current index is odd and the next value is still within the range of A
            # We will keep iterating until we see an even value for replacement
            while A[idx] % 2 == 1 and next_val < len(A):
                # Hence if we found the next even value after the odd value,
                if A[next_val] % 2 == 0:
                    # We swap the next odd and even value
                    A[idx], A[next_val] = A[next_val], A[idx]
                # else if the original idx + 1 value is not even, we will keep iterating through
                next_val += 1

        return A
