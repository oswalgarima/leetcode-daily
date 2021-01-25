"""
1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Example:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
"""


# Runtime: 4044ms
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Thought Process:
        # 1. In a very brute-force way, since we are always we are finding the maximum value from the right end
        # 2. We need to start from 2nd-index (index 1, given zero-indexing)
        # 3. We will enter a loop until we reach the last index
        # 4. Since at the last index, there is no more max_right value, we will then append -1 at the end

        pointer = 1
        temp_arr = []

        while pointer < len(arr):
            max_right = max(arr[pointer:])
            temp_arr.append(max_right)
            pointer += 1

        temp_arr.append(-1)

        return temp_arr
