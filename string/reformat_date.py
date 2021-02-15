"""
1507. Reformat Date
https://leetcode.com/problems/reformat-date/

Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.

Example:
Input: date = "20th Oct 2052"
Output: "2052-10-20"
"""


# Runtime: 32ms (60.25%)
class Solution:
    def reformatDate(self, date: str) -> str:

        month_string = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_map = dict(zip(month_string, [str(i).zfill(2) for i in range(1, 13)]))

        temp = date.split(' ')

        year = temp[-1]
        month = month_map[temp[1]]
        day = temp[0][:-2].zfill(2)

        return f"{year}-{month}-{day}"
