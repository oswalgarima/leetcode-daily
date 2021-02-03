"""
1491. Average Salary Excluding the Minimum and Maximum Salary
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.


Example:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000
"""


# Runtime: 40ms (18.22%)
class Solution:
    def average(self, salary: List[int]) -> float:

        salary.sort()

        # float as fast/faster than int()
        return float(sum(salary[1:-1]) / (len(salary[1:-1])))
