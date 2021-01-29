"""
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


Given an array of integers numbers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer
array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.


Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


# Runtime: 64ms
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Using a two pointer approach where we converge towards the middle
        i, j = 0, len(numbers) - 1

        while True:
            # if the front and back number sum > target, this means we need to decrease the summation
            # We decrease the summation by going backwards on the back pointer since the arr is sorted
            if numbers[i] + numbers[j] > target:
                j -= 1
            # Likewise, since we are below the target, we need to increase the front pointer to add on to the summation to reach the target
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                break

        # Since 1-indexed, we need to + 1 to zero-indexed
        return [i+1, j+1]
