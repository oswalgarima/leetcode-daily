"""
1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies,
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids
such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.

Example:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy, therefore only kid 1 will have
the greatest number of candies among the kids regardless of
who takes the extra candy.
"""


# Runtime: 44ms
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        arr = []

        for candy in candies:
            increase_candy = candy + extraCandies
            arr.append(increase_candy >= max(candies))

        return arr
