"""
1089. Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/


Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""


# Runtime: 124ms
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # Thought Process:
        # 1. We need a counter to take note of the current position that we are in
        # 2. For every zero we duplicate, we need to remove 1 val from the back
        # 3. Because it is inplace, and our array is of an fix length

        # Counter to keep track of index
        count = 0

        # Count cannot exceed the total fix length
        while count < len(arr):
            if arr[count] == 0:
                # To insert a duplicated zero on the right side, while pushing the elements right
                arr.insert(count+1, 0)
                # To remove a value from the back to to preserve the fix length
                arr.pop()
                # Hence if you add one value to the right, the next val is a 0
                # To prevent duplication, we need to increase position counter by 2 instead
                # To skip the recently duplicated 0
                count += 2
            else:
                # if all else normal, we just need increase index by 1
                count += 1
