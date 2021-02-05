"""
1323. Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit
(6 becomes 9, and 9 becomes 6).


Example:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
"""


# Runtime: 36ms (17.72%)
class Solution:
    def maximum69Number(self, num: int) -> int:

        # we need to change the first number that is 6
        # because coming from left means coming from a bigger number
        # hence once we meet the first 6, we can change it to 9
        # and return the number

        arr = list(str(num))

        for idx, val in enumerate(arr):
            if val == '6':
                arr[idx] = '9'
                break

        return int(''.join(arr))
