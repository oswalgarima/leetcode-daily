"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""



# Runtime: 32ms (56.14%)
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0 for i in range(n+1)]

        # takes 1 step for 0 steps (you take no steps)
        dp[0] = 1
        # takes 1 step for 1 step (you take only 1 steps)
        dp[1] = 1

        for i in range(2, n+1):
            # you can only either start from
            # 1 step or 2 step back
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

            
