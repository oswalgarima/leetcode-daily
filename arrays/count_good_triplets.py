"""
1534. Count Good Triplets
https://leetcode.com/problems/count-good-triplets/

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

Example:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
"""


# Runtime: 828ms
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        count = 0

        for i in range(0, len(arr) - 2):
            for j in range(i+1, len(arr) - 1):
                if (abs(arr[j] - arr[i]) <= a):
                    # have to j+1 as we might have skip another value of i if it failed the previous if statement
                    for k in range(j+1, len(arr)):
                        # True = 1, False = 0
                        count += abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c
                else:
                    continue

        return count
