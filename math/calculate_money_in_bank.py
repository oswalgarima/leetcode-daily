"""
1716. Calculate Money in Leetcode Bank
https://leetcode.com/problems/calculate-money-in-leetcode-bank/

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
Notice that on the 2nd Monday, Hercy only puts in $2.
"""


# Runtime: 24ms (98.27%)
class Solution:
    def totalMoney(self, n: int) -> int:

        # if every 7 days pass, you gain 7 dollar more
        # base sum is (1 + 2 + 3 + 4 + 5 + 6 + 7) = 28
        # 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
        # 3 + 4 + 5 + 6 + 7 + 8 + 9 = 42

        quotient = n // 7
        remainder = n % 7
        output = 0

        for i in range(quotient):
            temp = 28 + i * 7
            output += temp

        for i in range(quotient+1, int(quotient + remainder + 1)):
            output += i

        return output
