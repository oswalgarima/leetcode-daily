"""
1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

# Runtime: 60ms


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        arr = []

        first_half = nums[:n]
        second_half = nums[n:]

        count = 0
        while count < n:
            arr.append(first_half[count])
            arr.append(second_half[count])
            count += 1

        return arr
