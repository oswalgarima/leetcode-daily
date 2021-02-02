"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.


Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""


# Runtime: 124ms (11.62%)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(reverse=False, key=lambda x: x[0])

        # keep track of the non-overlapping interval
        output = []

        # looping through each interval
        for idx, interval in enumerate(intervals):
            # if the output list is empty or the last output is not overlapping with current interval
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            # else if last output interval overlaps with current interval
            else:
                # we need to check which interval's last val is bigger
                output[-1][1] = max(output[-1][1], interval[1])

        return output
