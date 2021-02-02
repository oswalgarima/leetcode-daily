"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/


Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.


Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


# Runtime: 68ms (99.02%)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # assumed that start time has been sorted
        output = []
        i = 0

        # This runs as long as current interval in intervals is started earlier than new interval
        # Append existing intervals into output if interval[i][0] < newInterval[0]
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            output.append(intervals[i])
            i += 1
            # breaks when not more interval[i][0] < newInterval[0]

        # if new interval starts earlier instead, you need to append newInterval
        # lastly, if there's an overlap you need to swap accordingly
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            # we need to merge if the output[-1][1] > newInterval[0] -> there's an overlap
            output[-1][1] = max(output[-1][1], newInterval[1])

        while i < len(intervals):
            if output[-1][1] < intervals[i][0]:
                output.append(intervals[i])
            else:
                # once you inserted the newInterval, now you need compare with next element in intervals
                # your latest merged output[-1][1] > interval[i][0] -> that means you still need to merge
                output[-1][1] = max(output[-1][1], intervals[i][1])
            i += 1

        return output
