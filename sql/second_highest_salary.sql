/*
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

Write a SQL query to get the second highest salary from the Employee table.

Schema:
Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (Id, Salary) values ('1', '100')
insert into Employee (Id, Salary) values ('2', '200')
insert into Employee (Id, Salary) values ('3', '300')
*/

-- Runtime: 164ms
-- Write your MySQL query statement below

-- Selecting salary if no 2nd highest -> return null, hence no special treatment
SELECT MAX(salary) AS SecondHighestSalary
FROM employee
-- Using WHERE to filter out the top salary first
WHERE salary NOT IN (
    SELECT MAX(salary)
    FROM employee
)
